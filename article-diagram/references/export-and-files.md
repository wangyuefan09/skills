# Draw.io 导出与文件规范

本文件定义 article-diagram 的导出命令、命名约定和交付规则。只有在需要落文件、导出或打开图表时再读取。

## 标准流程

1. 先生成 `.drawio`
2. 检测本机是否存在 `drawio` CLI
3. 若用户要求导出，则执行对应导出命令；文章 PNG 默认使用 2 倍导出
4. 返回 `.drawio` 路径和导出文件路径
5. 若导出失败，不删除 `.drawio`

## 检测命令

```bash
# macOS/Linux
which drawio

# Windows
where drawio
```

## 导出命令

```bash
# 公众号正文 PNG：2 倍导出，保留 20px 边距
drawio -x -f png -s 2 -b 20 -o output.png input.drawio

# SVG 导出
drawio -x -f svg -b 20 -o output.svg input.drawio

# PDF 导出
drawio -x -f pdf -b 20 -o output.pdf input.drawio
```

## 打开文件

```bash
# macOS
open filename.drawio

# Linux
xdg-open filename.drawio

# Windows
start filename.drawio
```

## 文件命名规范

| 场景 | 命名格式 | 示例 |
|-----|---------|------|
| 流程图 | `{name}-flow.drawio` | `login-flow.drawio` |
| 架构图 | `{name}-arch.drawio` | `system-arch.drawio` |
| 时序图 | `{name}-seq.drawio` | `api-call-seq.drawio` |
| ER 图 | `{name}-er.drawio` | `user-db-er.drawio` |
| 状态图 | `{name}-state.drawio` | `order-state.drawio` |
| 思维导图 | `{name}-mind.drawio` | `rag-mind.drawio` |
| 导出 PNG | `{name}.png` | `login-flow.png` |
| 导出 SVG | `{name}.svg` | `system-arch.svg` |
| 导出 PDF | `{name}.pdf` | `api-doc.pdf` |

## 交付规则

- 若用户只说“生成图”，默认交付 `.drawio`
- 若用户明确说“导出 PNG/SVG/PDF”，同时交付 `.drawio` 和导出文件
- 若本机没有 `drawio` CLI，要明确说明未自动导出，并把建议命令返回给用户
- 如果用户要求“只保留导出产物”，删除 `.drawio` 前先确认导出成功
- 文章图片使用干净的 `.png` 文件名；可编辑能力由单独保留的 `.drawio` 源文件提供

## 临时渲染验收

多页文件交付前，按以下规则逐页检查：

- 本机存在 draw.io CLI 时，以 2 倍缩放和 20px 边距逐页导出临时 PNG。
- 检查节点文字、连线标签、反馈路径、箭头方向和容器边界。
- 临时预览只用于验收；用户未要求导出时，不把临时文件作为交付物。
- 发现文字覆盖、线段穿过节点或无意义交叉时，返回 XML 调整布局并重新预览。
- XML 解析、ID、引用和画布边界检查通过，不代表视觉验收通过。
- 本机没有 draw.io CLI 时，运行严格几何校验并明确说明未完成渲染预览。
