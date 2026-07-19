# Draw.io XML 与布局规范

本文件包含 XML 结构规则、文本标签约束、节点与连线模板，以及不同图表类型的布局建议。只有在需要生成或修改 `.drawio` XML 时再读取。

## 文本标签规则

- `mxCell` 的 `value` 中禁止使用 HTML 标签，例如 `&lt;b&gt;`、`&lt;/b&gt;`、`&lt;br&gt;`、`<b>`、`<br>`。
- 需要换行时使用 XML 换行实体 `&#xa;`。
- 需要强调文字时使用 `fontStyle=1` 或拆成独立文本节点。
- 文本和图形节点优先设置 `html=0`。
- 生成后检查文件中是否残留 HTML 标签。

## 连线标签规则

- 短连接线不放长标签，必要时只保留协议、事件名或“是 / 否”等短词。
- 原因和长说明优先写进节点或正文。
- 连线标签不得覆盖箭头主体。

## 画布选择

| 场景 | pageWidth | pageHeight |
| --- | ---: | ---: |
| 默认纵向页面 | `827` | `1169` |
| 横向架构与调用关系 | `1000` | `700` |

优先使用原版纵向页面；只有结构天然横向时才使用横向画布。

## 基础模板

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2025-01-01T00:00:00.000Z" agent="article-diagram" version="24.0.0">
  <diagram name="Page-1" id="diagram-id">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0" background="#F7F9FC">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- 图表内容 -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## 标题样式模板

主标题使用 `fontSize=20`。节点、容器标题和连线标签统一使用 `fontSize=15`。

```xml
<mxCell id="title" value="图表标题" style="text;html=0;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=20;fontStyle=1;fontColor=#2D3748;" vertex="1" parent="1">
  <mxGeometry x="260" y="20" width="300" height="40" as="geometry"/>
</mxCell>
```

## 节点样式模板

### 通用节点

```xml
<mxCell id="node-id" value="节点名称" style="rounded=1;whiteSpace=wrap;html=0;fillColor={类别填充色};strokeColor=none;fontColor={类别文字色};fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;shadow=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="60" as="geometry"/>
</mxCell>
```

### 常见节点

```xml
<mxCell id="client-id" value="客户端" style="rounded=1;whiteSpace=wrap;html=0;fillColor=#1889A2;strokeColor=none;fontColor=#FFFFFF;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;shadow=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="60" as="geometry"/>
</mxCell>

<mxCell id="gateway-id" value="API 网关" style="rounded=1;whiteSpace=wrap;html=0;fillColor=#0B6170;strokeColor=none;fontColor=#FFFFFF;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;shadow=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="60" as="geometry"/>
</mxCell>

<mxCell id="service-id" value="用户服务" style="rounded=1;whiteSpace=wrap;html=0;fillColor=#D9864F;strokeColor=none;fontColor=#FFFFFF;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;shadow=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="60" as="geometry"/>
</mxCell>

<mxCell id="infra-id" value="认证服务" style="rounded=1;whiteSpace=wrap;html=0;fillColor=#6F5CC2;strokeColor=none;fontColor=#FFFFFF;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;shadow=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="140" height="60" as="geometry"/>
</mxCell>

<mxCell id="db-id" value="MySQL 主库" style="shape=cylinder3;whiteSpace=wrap;html=0;fillColor=#D9864F;strokeColor=none;fontColor=#FFFFFF;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;shadow=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="80" as="geometry"/>
</mxCell>

<mxCell id="decision-id" value="条件?" style="rhombus;whiteSpace=wrap;html=0;fillColor=#0B6170;strokeColor=none;fontColor=#FFFFFF;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;shadow=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="200" width="120" height="80" as="geometry"/>
</mxCell>

<mxCell id="group-id" value="服务集群" style="swimlane;whiteSpace=wrap;html=0;fillColor=none;strokeColor=#0B6170;dashed=1;strokeWidth=2;fontColor=#2D3748;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;" vertex="1" parent="1">
  <mxGeometry x="50" y="50" width="400" height="250" as="geometry"/>
</mxCell>
```

## 连线样式模板

```xml
<mxCell id="edge-id" value="HTTP" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=0;endArrow=block;endFill=1;strokeWidth=2;strokeColor=#94A3B8;labelBackgroundColor=#F7F9FC;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;fontColor=#64748B;" edge="1" source="source-id" target="target-id" parent="1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

```xml
<mxCell id="edge-id" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=0;endArrow=block;endFill=1;strokeWidth=2;strokeColor=#94A3B8;" edge="1" source="source-id" target="target-id" parent="1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

```xml
<mxCell id="edge-id" value="异步消息" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=0;endArrow=block;endFill=1;dashed=1;strokeWidth=2;strokeColor=#94A3B8;labelBackgroundColor=#F7F9FC;fontFamily=system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif;fontSize=15;fontColor=#64748B;" edge="1" source="source-id" target="target-id" parent="1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## 图表类型布局建议

### 流程图

- 主干保持单向阅读，优先从上到下。
- 分支判断使用菱形，出口只保留短标签。
- 不用装饰性卡片包裹每个步骤。

### 架构图

- 先画层，再画层内节点。
- 相同职责的节点放进同一容器。
- 外部依赖和内部模块拉开层次。

### 时序图

- 参与者从左到右，消息自上而下。
- 横向过宽时拆分主链路和异常链路。

### ER 图

- 实体名清晰，主键和外键关系明确。
- 复杂系统按子域拆图。

### 状态机图

- 状态是节点，事件是边。
- 开始和结束状态要明显。

### 思维导图

- 第一层分支控制在 4-8 个。
- 同层级节点保持一致。

## 多页文章配图

- 每页根据内容选择最自然的构图，不复制同一套装饰骨架。
- 页面之间通过颜色、字体、节点和连线保持统一。
- 不默认添加编号徽章、彩色短线或总结条。

## XML 注意事项

1. 每个 `mxCell` 必须有唯一 `id`。
2. 每条边必须有明确的 `source` 和 `target`。
3. 特殊字符必须转义：`&amp;` `&lt;` `&gt;` `&quot;`。
4. XML 注释中不能使用 `--`。
5. 使用网格对齐，建议以 10px 为单位。
6. 精细控制连线时使用 `entryX/entryY`。

## 连线与文字防碰撞规则

### 先分配通道，再放置节点

- 保持主流程单向阅读，将反馈线、重试线和重规划线放到页面外侧或层间空隙。
- 让反馈通道与非起终点节点至少保持 `16px` 距离，让平行连线之间至少保持 `20px` 距离。
- 为页面外侧回程通道预留至少 `30px` 空间。
- 不得使用其他节点的水平或垂直中心轴作为路由通道。
- 为不同方向的反馈线分配不同通道，避免共线重叠或在节点附近交叉。

### 限制自动路由

- 只对同一行或同一列的相邻节点使用自动正交路由。
- 为反馈线、跨层连线、对角连线和带标签的复杂连线显式设置 `exitX`、`exitY`、`entryX`、`entryY`。
- 为复杂连线提供足够的 `mxPoint` 拐点，使每段路径都能在 XML 中确定。
- 检查相邻拐点是否形成明确的水平线或垂直线；不要依赖渲染器猜测折线方向。
- 将节点边界按 `16px` 向外扩展后，任何非起终点连线都不得进入该区域。

```xml
<mxCell id="feedback-edge" value="重规划" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=0;endArrow=block;strokeWidth=2;strokeColor=#94A3B8;exitX=0.5;exitY=1;entryX=0;entryY=0.5;" edge="1" source="decision" target="planner" parent="1">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="500" y="460"/>
      <mxPoint x="180" y="460"/>
      <mxPoint x="180" y="150"/>
    </Array>
  </mxGeometry>
</mxCell>
```

### 放置连线标签

- 只在长度不少于 `80px` 的空白线段上放置标签。
- 让标签边界与节点至少保持 `8px` 距离，并避免标签与标签相交。
- 只保留“调用”“结果”“是”“否”等帮助理解关系的短标签。
- 节点关系已经能表达的“领取”“判断”“步骤完成”等标签优先删除。
- 找不到安全位置时，将说明移入节点或使用独立文本节点，不要让标签覆盖节点正文。

### 处理过密页面

出现两条以上反馈回路，或无法为连线分配独立通道时，按顺序处理：

1. 改为分层布局，将规划、执行、反馈等职责放到不同层。
2. 增大节点间距，为正向流和回程流建立独立通道。
3. 删除重复的连线标签。
4. 仍然拥挤时拆分页面。

### 执行几何校验

生成或修改文件后运行：

```bash
python <article-diagram-skill-root>/scripts/validate_drawio_layout.py output.drawio --strict
```

该脚本负责检查确定性几何问题。复杂连线缺少显式端口或拐点时，严格模式必须失败，因为仅凭 XML 无法推导 draw.io 最终采用的自动路径。
