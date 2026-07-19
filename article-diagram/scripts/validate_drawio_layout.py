#!/usr/bin/env python3
"""Check deterministic layout collisions in uncompressed draw.io XML."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


EPS = 1e-6
HTML_RE = re.compile(r"</?(?:b|br|div|span|p)\b", re.IGNORECASE)
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
Issue = tuple[str, str, str, str]  # severity, page, code, message
Point = tuple[float, float]


@dataclass(frozen=True)
class Rect:
    cell_id: str
    x: float
    y: float
    width: float
    height: float

    @property
    def right(self) -> float:
        return self.x + self.width

    @property
    def bottom(self) -> float:
        return self.y + self.height

    @property
    def center(self) -> Point:
        return (self.x + self.width / 2, self.y + self.height / 2)

    def inflate(self, amount: float) -> "Rect":
        return Rect(
            self.cell_id,
            self.x - amount,
            self.y - amount,
            self.width + amount * 2,
            self.height + amount * 2,
        )


def number(value: str | None, default: float = 0.0) -> float:
    try:
        return float(value) if value not in (None, "") else default
    except ValueError:
        return default


def style_map(raw: str | None) -> dict[str, str]:
    result: dict[str, str] = {}
    for token in (raw or "").split(";"):
        token = token.strip()
        if not token:
            continue
        key, separator, value = token.partition("=")
        result[key] = value if separator else "1"
    return result


def overlaps(first: Rect, second: Rect) -> bool:
    return (
        first.x < second.right - EPS
        and first.right > second.x + EPS
        and first.y < second.bottom - EPS
        and first.bottom > second.y + EPS
    )


def segment_hits_rect(start: Point, end: Point, rect: Rect) -> bool:
    if abs(start[1] - end[1]) <= EPS:
        return (
            rect.y - EPS <= start[1] <= rect.bottom + EPS
            and max(min(start[0], end[0]), rect.x)
            <= min(max(start[0], end[0]), rect.right) + EPS
        )
    if abs(start[0] - end[0]) <= EPS:
        return (
            rect.x - EPS <= start[0] <= rect.right + EPS
            and max(min(start[1], end[1]), rect.y)
            <= min(max(start[1], end[1]), rect.bottom) + EPS
        )
    return False


def segment_relation(
    first_start: Point,
    first_end: Point,
    second_start: Point,
    second_end: Point,
) -> str | None:
    first_horizontal = abs(first_start[1] - first_end[1]) <= EPS
    second_horizontal = abs(second_start[1] - second_end[1]) <= EPS

    if first_horizontal and second_horizontal:
        if abs(first_start[1] - second_start[1]) > EPS:
            return None
        length = min(max(first_start[0], first_end[0]), max(second_start[0], second_end[0])) - max(
            min(first_start[0], first_end[0]), min(second_start[0], second_end[0])
        )
        return "overlap" if length > EPS else None

    if not first_horizontal and not second_horizontal:
        if abs(first_start[0] - second_start[0]) > EPS:
            return None
        length = min(max(first_start[1], first_end[1]), max(second_start[1], second_end[1])) - max(
            min(first_start[1], first_end[1]), min(second_start[1], second_end[1])
        )
        return "overlap" if length > EPS else None

    horizontal = (first_start, first_end) if first_horizontal else (second_start, second_end)
    vertical = (second_start, second_end) if first_horizontal else (first_start, first_end)
    if (
        min(horizontal[0][0], horizontal[1][0]) - EPS
        <= vertical[0][0]
        <= max(horizontal[0][0], horizontal[1][0]) + EPS
        and min(vertical[0][1], vertical[1][1]) - EPS
        <= horizontal[0][1]
        <= max(vertical[0][1], vertical[1][1]) + EPS
    ):
        return "cross"
    return None


def absolute_vertices(
    cells: list[ET.Element],
) -> tuple[dict[str, tuple[Rect, bool]], dict[str, ET.Element]]:
    cell_by_id = {cell.get("id", ""): cell for cell in cells if cell.get("id")}
    cache: dict[str, tuple[Rect, bool]] = {}
    active: set[str] = set()

    def resolve(cell_id: str) -> tuple[Rect, bool] | None:
        if cell_id in cache:
            return cache[cell_id]
        if cell_id in active:
            return None
        cell = cell_by_id.get(cell_id)
        if cell is None or cell.get("vertex") != "1":
            return None
        geometry = cell.find("mxGeometry")
        if geometry is None:
            return None

        active.add(cell_id)
        x = number(geometry.get("x"))
        y = number(geometry.get("y"))
        parent = resolve(cell.get("parent", ""))
        if parent:
            x += parent[0].x
            y += parent[0].y
        style = style_map(cell.get("style"))
        result = (
            Rect(
                cell_id,
                x,
                y,
                number(geometry.get("width")),
                number(geometry.get("height")),
            ),
            "swimlane" in style
            or style.get("container") == "1"
            or style.get("group") == "1",
        )
        active.remove(cell_id)
        cache[cell_id] = result
        return result

    for cell_id in cell_by_id:
        resolve(cell_id)
    return cache, cell_by_id


def waypoints(geometry: ET.Element | None) -> list[Point]:
    if geometry is None:
        return []
    for array in geometry.findall("Array"):
        if array.get("as") == "points":
            return [
                (number(point.get("x")), number(point.get("y")))
                for point in array.findall("mxPoint")
            ]
    return []


def boundary(rect: Rect, toward: Point) -> Point:
    center_x, center_y = rect.center
    dx, dy = toward[0] - center_x, toward[1] - center_y
    if abs(dx) <= EPS and abs(dy) <= EPS:
        return (rect.right, center_y)
    x_scale = float("inf") if abs(dx) <= EPS else rect.width / 2 / abs(dx)
    y_scale = float("inf") if abs(dy) <= EPS else rect.height / 2 / abs(dy)
    scale = min(x_scale, y_scale)
    return (center_x + dx * scale, center_y + dy * scale)


def port(rect: Rect, style: dict[str, str], prefix: str, toward: Point) -> Point:
    if f"{prefix}X" in style and f"{prefix}Y" in style:
        return (
            rect.x + rect.width * number(style[f"{prefix}X"], 0.5),
            rect.y + rect.height * number(style[f"{prefix}Y"], 0.5),
        )
    return boundary(rect, toward)


def path_midpoint(points: list[Point], fraction: float) -> tuple[Point, float]:
    segments = [
        (start, end, abs(end[0] - start[0]) + abs(end[1] - start[1]))
        for start, end in zip(points, points[1:])
    ]
    total = sum(length for _, _, length in segments)
    remaining = max(0.0, min(1.0, fraction)) * total
    for start, end, length in segments:
        if remaining <= length + EPS:
            ratio = 0 if length <= EPS else remaining / length
            return (
                (
                    start[0] + (end[0] - start[0]) * ratio,
                    start[1] + (end[1] - start[1]) * ratio,
                ),
                length,
            )
        remaining -= length
    return points[-1], segments[-1][2] if segments else 0


def label_rect(
    edge_id: str,
    label: str,
    points: list[Point],
    geometry: ET.Element | None,
    font_size: float,
) -> tuple[Rect, float]:
    relative_x = number(geometry.get("x") if geometry is not None else None)
    center, host_length = path_midpoint(points, (relative_x + 1) / 2)
    offset_x = 0.0
    offset_y = number(geometry.get("y") if geometry is not None else None)
    if geometry is not None:
        for point in geometry.findall("mxPoint"):
            if point.get("as") == "offset":
                offset_x += number(point.get("x"))
                offset_y += number(point.get("y"))

    lines = label.splitlines() or [label]
    widths = []
    for line in lines:
        units = sum(
            1.0
            if unicodedata.east_asian_width(char) in {"W", "F", "A"}
            else 0.35
            if char.isspace()
            else 0.6
            for char in line
        )
        widths.append(units * font_size)
    width = max(24.0, max(widths) + 10)
    height = max(22.0, len(lines) * font_size * 1.4 + 6)
    return (
        Rect(
            f"label:{edge_id}",
            center[0] + offset_x - width / 2,
            center[1] + offset_y - height / 2,
            width,
            height,
        ),
        host_length,
    )


def validate_page(
    diagram: ET.Element,
    multi_page: bool,
    clearance: float,
    min_label_segment: float,
) -> list[Issue]:
    page = diagram.get("name") or "<unnamed>"
    model = diagram.find("mxGraphModel")
    if model is None:
        return [("ERROR", page, "MODEL", "diagram must contain an uncompressed mxGraphModel")]
    root = model.find("root")
    if root is None:
        return [("ERROR", page, "ROOT", "mxGraphModel has no root")]

    issues: list[Issue] = []
    cells = root.findall("mxCell")
    vertices, cell_by_id = absolute_vertices(cells)
    obstacles = [(cell_id, data[0]) for cell_id, data in vertices.items() if not data[1]]
    edges = [cell for cell in cells if cell.get("edge") == "1"]

    for cell_id, count in Counter(
        cell.get("id") for cell in cells if cell.get("id")
    ).items():
        if count > 1:
            issues.append(("ERROR", page, "DUPLICATE_ID", f"duplicate cell id {cell_id!r}"))
    if multi_page and not KEBAB_RE.fullmatch(page):
        issues.append(("WARNING", page, "PAGE_NAME", "page name is not lowercase kebab-case"))

    page_width = number(model.get("pageWidth"), float("inf"))
    page_height = number(model.get("pageHeight"), float("inf"))
    for cell_id, (rect, _) in vertices.items():
        if rect.x < 0 or rect.y < 0 or rect.right > page_width or rect.bottom > page_height:
            issues.append(("ERROR", page, "OUT_OF_BOUNDS", f"vertex {cell_id!r} is outside the page"))
    for cell in cells:
        if HTML_RE.search(cell.get("value") or ""):
            issues.append(("ERROR", page, "HTML_VALUE", f"cell {cell.get('id', '')!r} contains HTML"))

    for index, (first_id, first) in enumerate(obstacles):
        for second_id, second in obstacles[index + 1 :]:
            if overlaps(first, second):
                issues.append(
                    ("ERROR", page, "NODE_OVERLAP", f"vertices {first_id!r} and {second_id!r} overlap")
                )

    paths: list[dict[str, object]] = []
    auto_count = 0
    for edge in edges:
        edge_id = edge.get("id", "")
        source_id, target_id = edge.get("source", ""), edge.get("target", "")
        if source_id not in cell_by_id or target_id not in cell_by_id:
            issues.append(("ERROR", page, "BAD_REFERENCE", f"edge {edge_id!r} has a missing endpoint"))
            continue
        if source_id not in vertices or target_id not in vertices:
            issues.append(("ERROR", page, "BAD_ENDPOINT", f"edge {edge_id!r} endpoint has no geometry"))
            continue

        geometry = edge.find("mxGeometry")
        route = waypoints(geometry)
        style = style_map(edge.get("style"))
        source, target = vertices[source_id][0], vertices[target_id][0]
        same_row = abs(source.center[1] - target.center[1]) <= EPS
        same_column = abs(source.center[0] - target.center[0]) <= EPS
        if not route:
            auto_count += 1
            if not (same_row or same_column):
                issues.append(
                    ("WARNING", page, "COMPLEX_AUTO_ROUTE", f"edge {edge_id!r} is diagonal and automatic")
                )
                continue
        elif not all(key in style for key in ("exitX", "exitY", "entryX", "entryY")):
            issues.append(
                ("WARNING", page, "MISSING_PORTS", f"edge {edge_id!r} has waypoints without explicit ports")
            )

        source_toward = route[0] if route else target.center
        target_toward = route[-1] if route else source.center
        points = [
            port(source, style, "exit", source_toward),
            *route,
            port(target, style, "entry", target_toward),
        ]
        points = [
            point
            for index, point in enumerate(points)
            if index == 0 or point != points[index - 1]
        ]
        if any(
            abs(start[0] - end[0]) > EPS and abs(start[1] - end[1]) > EPS
            for start, end in zip(points, points[1:])
        ):
            issues.append(
                ("WARNING", page, "AMBIGUOUS_PATH", f"edge {edge_id!r} has non-axis-aligned segments")
            )
            continue
        paths.append(
            {
                "id": edge_id,
                "source": source_id,
                "target": target_id,
                "label": (edge.get("value") or "").strip(),
                "points": points,
                "geometry": geometry,
                "font_size": number(style.get("fontSize"), 15),
            }
        )

    if (len(obstacles) > 8 or len(edges) > 10) and auto_count == len(edges):
        issues.append(("WARNING", page, "DENSE_AUTO_ROUTING", "dense page is fully automatic"))

    for path in paths:
        points = path["points"]
        assert isinstance(points, list)
        for start, end in zip(points, points[1:]):
            for cell_id, rect in obstacles:
                if cell_id in {path["source"], path["target"]}:
                    continue
                if segment_hits_rect(start, end, rect.inflate(clearance)):
                    issues.append(
                        (
                            "ERROR",
                            page,
                            "EDGE_NODE_COLLISION",
                            f"edge {path['id']!r} crosses vertex {cell_id!r} clearance",
                        )
                    )
                    break

    for index, first in enumerate(paths):
        for second in paths[index + 1 :]:
            if {first["source"], first["target"]} & {second["source"], second["target"]}:
                continue
            relation = next(
                (
                    relation
                    for first_segment in zip(first["points"], first["points"][1:])
                    for second_segment in zip(second["points"], second["points"][1:])
                    if (
                        relation := segment_relation(
                            first_segment[0],
                            first_segment[1],
                            second_segment[0],
                            second_segment[1],
                        )
                    )
                ),
                None,
            )
            if relation:
                issues.append(
                    (
                        "WARNING",
                        page,
                        "EDGE_EDGE_COLLISION",
                        f"edges {first['id']!r} and {second['id']!r} {relation}",
                    )
                )

    labels: list[tuple[str, Rect]] = []
    for path in paths:
        if not path["label"]:
            continue
        rect, host_length = label_rect(
            str(path["id"]),
            str(path["label"]),
            path["points"],
            path["geometry"],
            float(path["font_size"]),
        )
        labels.append((str(path["id"]), rect))
        if host_length < min_label_segment:
            issues.append(
                (
                    "WARNING",
                    page,
                    "SHORT_LABEL_SEGMENT",
                    f"edge {path['id']!r} label host is {host_length:.1f}px",
                )
            )
        for cell_id, node in obstacles:
            if overlaps(rect, node.inflate(8)):
                issues.append(
                    (
                        "ERROR",
                        page,
                        "LABEL_NODE_COLLISION",
                        f"edge {path['id']!r} label overlaps vertex {cell_id!r}",
                    )
                )
                break

    for index, (first_id, first) in enumerate(labels):
        for second_id, second in labels[index + 1 :]:
            if overlaps(first, second):
                issues.append(
                    (
                        "WARNING",
                        page,
                        "LABEL_LABEL_COLLISION",
                        f"labels on edges {first_id!r} and {second_id!r} overlap",
                    )
                )
    return issues


def validate(path: Path, clearance: float, min_label_segment: float) -> tuple[list[Issue], int]:
    try:
        root = ET.parse(path).getroot()
    except (OSError, ET.ParseError) as error:
        return [("ERROR", "<file>", "XML_PARSE", str(error))], 0
    if root.tag != "mxfile":
        return [("ERROR", "<file>", "ROOT_ELEMENT", "root must be mxfile")], 0

    diagrams = root.findall("diagram")
    if not diagrams:
        return [("ERROR", "<file>", "NO_DIAGRAM", "mxfile has no diagram")], 0

    issues: list[Issue] = []
    for name, count in Counter(
        diagram.get("name") or "<unnamed>" for diagram in diagrams
    ).items():
        if count > 1:
            issues.append(("ERROR", "<file>", "DUPLICATE_PAGE", f"duplicate page {name!r}"))
    for diagram in diagrams:
        issues.extend(
            validate_page(
                diagram,
                len(diagrams) > 1,
                clearance,
                min_label_segment,
            )
        )
    return issues, len(diagrams)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate collisions and deterministic routing in draw.io XML."
    )
    parser.add_argument("drawio", type=Path, help="uncompressed .drawio file")
    parser.add_argument("--strict", action="store_true", help="fail on warnings")
    parser.add_argument("--clearance", type=float, default=16.0)
    parser.add_argument("--min-label-segment", type=float, default=80.0)
    args = parser.parse_args()

    issues, page_count = validate(
        args.drawio,
        args.clearance,
        args.min_label_segment,
    )
    for severity, page, code, message in issues:
        stream = sys.stderr if severity == "ERROR" else sys.stdout
        print(f"{severity} [{page}] {code}: {message}", file=stream)

    errors = sum(issue[0] == "ERROR" for issue in issues)
    warnings = sum(issue[0] == "WARNING" for issue in issues)
    failed = errors > 0 or (args.strict and warnings > 0)
    print(
        f"{'FAIL' if failed else 'PASS'}: "
        f"pages={page_count} errors={errors} warnings={warnings}"
    )
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
