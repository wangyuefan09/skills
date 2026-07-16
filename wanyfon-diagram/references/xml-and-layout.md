# Draw.io XML And Layout Rules

Use this reference when creating or editing `.drawio` files.

## XML Structure

Prefer uncompressed diagrams.net XML so it can be reviewed and patched easily:

```xml
<mxfile host="app.diagrams.net" agent="Codex" version="24.8.0">
  <diagram id="page-1" name="Page-1">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="900" math="0" shadow="0">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

Every visible cell must have:

- a deterministic `id`
- `parent="1"` or a container id
- `vertex="1"` with `mxGeometry` for nodes, or `edge="1"` with source/target for edges

Escape XML-sensitive characters in labels:

- `&` as `&amp;`
- `<` as `&lt;`
- `>` as `&gt;`
- double quotes inside attributes as `&quot;`

HTML line breaks in labels should use `&lt;br&gt;`.

## Style Snippets

Common node:

```text
rounded=1;whiteSpace=wrap;html=1;arcSize=8;shadow=0;fontFamily=Inter, PingFang SC, Microsoft YaHei, Arial;fontSize=12;fontColor=#1E2329;strokeWidth=1.5;spacing=10;spacingTop=7;spacingBottom=7;
```

Container:

```text
rounded=1;whiteSpace=wrap;html=1;arcSize=6;shadow=0;fillColor=#FFFFFF;strokeColor=#D0D5DD;strokeWidth=1.2;fontFamily=Inter, PingFang SC, Microsoft YaHei, Arial;fontSize=14;fontStyle=1;fontColor=#1F2937;align=left;verticalAlign=top;spacing=12;spacingTop=8;
```

Default edge:

```text
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeColor=#667085;strokeWidth=1.4;fontFamily=Inter, PingFang SC, Microsoft YaHei, Arial;fontSize=11;fontColor=#475467;
```

## Role Styles

Append these role values to the common node style:

```text
actor: fillColor=#F1F5F9;strokeColor=#64748B;fontColor=#1E293B;
gateway: fillColor=#E0F2FE;strokeColor=#0284C7;fontColor=#0C4A6E;
service: fillColor=#ECFDF5;strokeColor=#059669;fontColor=#064E3B;
worker: fillColor=#FEF3C7;strokeColor=#D97706;fontColor=#78350F;
database: shape=cylinder3d;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#F5F3FF;strokeColor=#7C3AED;fontColor=#4C1D95;
cache_queue: fillColor=#FFF7ED;strokeColor=#EA580C;fontColor=#7C2D12;
external: fillColor=#F8FAFC;strokeColor=#94A3B8;fontColor=#334155;dashed=1;
warning: fillColor=#FEF2F2;strokeColor=#DC2626;fontColor=#7F1D1D;
note: fillColor=#FFFFFF;strokeColor=#CBD5E1;fontColor=#334155;
```

## Layout Patterns

### Architecture / Request Flow

Use left-to-right columns:

| Column | X |
| --- | ---: |
| Actor / Client | 60 |
| Entry / Gateway | 280 |
| Core Services | 520 |
| Workers / Async | 760 |
| Data Stores | 980 |
| External Systems | 1180 |

Use row spacing of `100-120px`. Align related nodes horizontally where possible.

### Layered System

Use containers as horizontal bands:

- Edge / Client layer
- API / Integration layer
- Domain service layer
- Data / Infrastructure layer
- External dependency layer

Give each band `28px` horizontal padding and `36px` vertical padding.

### Process Flow

Use top-to-bottom layout:

- Start at `x=120, y=60`
- Step pitch: `100px`
- Decision nodes: diamond, `140 x 80`
- Keep yes/no branches symmetrical where possible

### Data Pipeline

Use left-to-right flow with stage groups:

- Source
- Ingest
- Transform
- Store
- Serve / Consume

Use dashed orange edges for async/event movement and purple edges for storage reads/writes.

## Geometry Rules

- Keep minimum horizontal gap between nodes: `48px`
- Keep minimum vertical gap between nodes: `36px`
- Edge labels should sit near the middle of the edge and not cover nodes.
- Do not place more than seven primary nodes in one row.
- If a diagram gets dense, split it into containers or multiple pages.
- Size containers after placing children, not before.

## Example Node

```xml
<mxCell id="svc-order" value="&lt;b&gt;订单服务&lt;/b&gt;&lt;br&gt;&lt;font style=&quot;font-size: 11px&quot;&gt;校验 / 编排 / 写入&lt;/font&gt;" style="rounded=1;whiteSpace=wrap;html=1;arcSize=8;shadow=0;fontFamily=Inter, PingFang SC, Microsoft YaHei, Arial;fontSize=12;fontColor=#064E3B;strokeWidth=1.5;spacing=10;spacingTop=7;spacingBottom=7;fillColor=#ECFDF5;strokeColor=#059669;" vertex="1" parent="1">
  <mxGeometry x="520" y="160" width="168" height="64" as="geometry"/>
</mxCell>
```

## Example Edge

```xml
<mxCell id="edge-api-order" value="REST" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeColor=#667085;strokeWidth=1.4;fontFamily=Inter, PingFang SC, Microsoft YaHei, Arial;fontSize=11;fontColor=#475467;" edge="1" parent="1" source="api-gateway" target="svc-order">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```
