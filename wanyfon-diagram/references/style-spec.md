# Wanyfon Clearline Style Spec

Use this style for all diagrams created by `wanyfon-diagram`.

## Visual Direction

The style should look like a clean engineering notebook prepared for a design review:

- compact but not crowded
- mostly flat, with no heavy shadows
- thin outlines and calm fills
- role-based colors instead of random decoration
- readable Chinese and English labels
- enough whitespace to scan flows quickly

Avoid glossy gradients, 3D effects, bright candy colors, decorative icons, and large card-like panels.

## Canvas

- Background: `#F7F8FA`
- Page grid: enabled when useful, but do not rely on visible grid lines
- Outer margin: at least `48px`
- Container padding: `28px` horizontal, `36px` vertical

## Typography

Use the following font preference:

`Inter, PingFang SC, Microsoft YaHei, Arial`

Draw.io style value:

`fontFamily=Inter, PingFang SC, Microsoft YaHei, Arial`

Text scale:

- Diagram title: `20px`, bold, `#111827`
- Container title: `14px`, bold, `#1F2937`
- Main node label: `12px`, bold when the node has a title
- Secondary detail: `11px`, regular, `#667085`
- Edge labels: `11px`, `#475467`

Do not use negative letter spacing. Keep labels under two lines when possible.

## Core Shape Style

Base node style:

```text
rounded=1;whiteSpace=wrap;html=1;arcSize=8;shadow=0;fontFamily=Inter, PingFang SC, Microsoft YaHei, Arial;fontSize=12;fontColor=#1E2329;strokeWidth=1.5;spacing=10;spacingTop=7;spacingBottom=7;
```

Default node geometry:

- Normal service: `168 x 64`
- Important gateway/service: `188 x 72`
- Small utility: `140 x 56`
- Data store: `150 x 64`
- Queue/cache: `150 x 58`
- External system: `168 x 64`

Use rounded rectangles for services and components. Use cylinders only for persistent databases when it improves recognition.

## Palette

Use fills softly and strokes decisively.

| Role | Fill | Stroke | Text |
| --- | --- | --- | --- |
| Actor / Client | `#F1F5F9` | `#64748B` | `#1E293B` |
| Gateway / API Entry | `#E0F2FE` | `#0284C7` | `#0C4A6E` |
| Core Service | `#ECFDF5` | `#059669` | `#064E3B` |
| Worker / Async Job | `#FEF3C7` | `#D97706` | `#78350F` |
| Data Store | `#F5F3FF` | `#7C3AED` | `#4C1D95` |
| Cache / Queue | `#FFF7ED` | `#EA580C` | `#7C2D12` |
| External System | `#F8FAFC` | `#94A3B8` | `#334155` |
| Security Boundary | `#EFF6FF` | `#2563EB` | `#1E3A8A` |
| Warning / Risk | `#FEF2F2` | `#DC2626` | `#7F1D1D` |
| Neutral Note | `#FFFFFF` | `#CBD5E1` | `#334155` |

Do not let a diagram become one-note. A typical architecture diagram should include neutral surfaces plus two or three semantic colors.

## Containers

Use containers for domains, layers, networks, teams, or environments.

Container style:

```text
rounded=1;whiteSpace=wrap;html=1;arcSize=6;shadow=0;fillColor=#FFFFFF;strokeColor=#D0D5DD;strokeWidth=1.2;fontFamily=Inter, PingFang SC, Microsoft YaHei, Arial;fontSize=14;fontStyle=1;fontColor=#1F2937;align=left;verticalAlign=top;spacing=12;spacingTop=8;
```

Container titles should be short: `Web 层`, `服务层`, `数据层`, `外部依赖`, `Control Plane`.

Use subtle tinted containers only for strong semantic boundaries:

- Internet / public zone: `#F0F9FF`
- Private network: `#F8FAFC`
- Security boundary: `#EFF6FF`
- Risk / fallback zone: `#FEF2F2`

## Edges

Default edge style:

```text
edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeColor=#667085;strokeWidth=1.4;fontFamily=Inter, PingFang SC, Microsoft YaHei, Arial;fontSize=11;fontColor=#475467;
```

Semantic edge variants:

- Synchronous request: solid `#475467`, width `1.4`
- Async event/message: dashed `#D97706`, width `1.4`, `dashed=1`
- Data read/write: solid `#7C3AED`, width `1.3`
- Control/config: dashed `#2563EB`, width `1.2`
- Error/fallback: dashed `#DC2626`, width `1.4`

Avoid crossing lines. If a crossing is unavoidable, route the lower-priority edge around the outside of the group.

## Labels

Preferred node label format:

```html
<b>API Gateway</b><br><font style="font-size: 11px">Auth / Rate Limit</font>
```

For Chinese:

```html
<b>订单服务</b><br><font style="font-size: 11px">校验 / 编排 / 写入</font>
```

Keep secondary text optional. Do not cram full sentences into nodes.

## Emphasis

Use emphasis sparingly:

- Important component: increase stroke width to `2`
- Current bottleneck/risk: use Warning role
- Selected path: use edge `strokeWidth=2`
- De-emphasized optional dependency: use dashed external style

Never use glow, large shadow, or heavy border as the default emphasis.
