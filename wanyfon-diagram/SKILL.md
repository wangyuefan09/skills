---
name: wanyfon-diagram
description: Create or edit clean draw.io/diagrams.net flowcharts, architecture diagrams, service dependency maps, request flows, data pipelines, and technical process diagrams using a personal Wanyfon Clearline visual style. Use when the user asks to draw, design, revise, or export a diagram as .drawio XML, or wants a polished technical diagram instead of plain Mermaid/ASCII.
---

# Wanyfon Diagram

## Purpose

Create diagrams.net/draw.io diagrams with a restrained, personal technical style: thin lines, soft fills, compact layout, readable Chinese/English labels, and clear role-based colors.

Prefer `.drawio` artifacts when the user asks for a diagram file. Use Mermaid only when the user explicitly asks for Mermaid or when no file artifact is needed.

## Workflow

1. Identify the diagram type: architecture, request flow, data pipeline, process flow, dependency map, deployment view, or decision flow.
2. Read `references/style-spec.md` before creating or restyling any visual diagram.
3. Read `references/xml-and-layout.md` when writing or editing `.drawio` XML.
4. Read `references/export-and-files.md` when saving files, naming outputs, validating XML, or exporting images.
5. Ask at most one clarification question only if the diagram cannot be inferred. Otherwise make a reasonable first version and state the assumption.
6. Generate valid diagrams.net XML with deterministic ids, stable geometry, and non-overlapping labels.
7. When editing an existing `.drawio`, preserve user content and only restyle or adjust the requested parts.

## Diagram Defaults

- Use one page unless the user requests multiple views.
- Keep labels short and concrete. Use Chinese labels naturally when the user's request is Chinese.
- Use containers for bounded contexts, layers, teams, regions, or runtime environments.
- Prefer left-to-right layout for architecture and request flow diagrams.
- Prefer top-to-bottom layout for stepwise processes and decision flows.
- Use arrow labels only when they clarify protocol, event name, or data semantics.
- Do not use decorative gradients, large shadows, stock illustrations, or dense icon art.

## Quality Bar

Before finishing, check that:

- The `.drawio` XML is parseable.
- Every edge has a clear source and target.
- Nodes do not overlap.
- Container bounds include their children with padding.
- The visual style follows `Wanyfon Clearline`, not a generic draw.io default.
- The final response names the created or changed file path.
