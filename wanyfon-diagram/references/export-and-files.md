# Export And File Rules

Use this reference when saving, validating, or exporting diagram files.

## File Naming

Use kebab-case names:

- `order-service-architecture.drawio`
- `rag-ingestion-pipeline.drawio`
- `payment-request-flow.drawio`

If the user gives a destination path, use it. Otherwise create a `diagrams/` directory in the current project and write the `.drawio` file there.

Do not overwrite an existing file unless the user asked to update it. If a same-name file exists, create a numbered variant such as `order-service-architecture-v2.drawio`.

## Validation

After writing a `.drawio` file:

1. Parse it as XML.
2. Check there is one `<mxfile>` root.
3. Check at least one `<diagram>` exists.
4. Check each edge with `source` and `target` points to an existing cell id.
5. Check visible vertex cells have `mxGeometry` with `x`, `y`, `width`, and `height`.

PowerShell XML parse check:

```powershell
[xml]$doc = Get-Content -Raw '.\diagrams\example.drawio'
$doc.mxfile.diagram.Count
```

## Exporting Images

Only export PNG/SVG/PDF if:

- the user explicitly asks for an image/PDF, or
- a diagrams.net CLI / draw.io CLI is already available locally.

If no CLI is available, still provide the `.drawio` file and state that image export was not run.

Do not rely on remote images or external icon URLs. Keep the diagram self-contained.

## Final Response

Keep the final response short:

- name the created or updated file
- mention validation status
- mention any skipped export or assumption

Example:

```text
已生成 diagrams/order-service-architecture.drawio，并通过 XML 解析检查。没有导出 PNG，因为本地没有可用的 draw.io CLI。
```
