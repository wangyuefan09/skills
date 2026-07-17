# Draw.io XML 与布局规范

本文件包含 XML 结构规则、文本标签约束、节点与连线模板，以及适合公众号和技术文章正文的布局建议。只有在需要生成或修改 `.drawio` XML 时再读取。

## 文本标签规则

- `mxCell` 的 `value` 中禁止使用 HTML 标签，例如 `&lt;b&gt;`、`&lt;/b&gt;`、`&lt;br&gt;`、`<b>`、`<br>`。
- 需要换行时使用 XML 换行实体 `&#xa;`，不要使用 `<br>` 或 `&lt;br&gt;`。
- 需要强调整段文字时使用样式字段，如 `fontStyle=1`，或拆成独立文本节点。
- 文本节点和图形节点默认使用纯文本渲染，样式中优先设置 `html=0`。
- 生成或修改 `.drawio` 后，必须检查文件中是否残留 HTML 标签，重点搜索 `&lt;`、`<b>`、`<br>`。
- 核心节点标签尽量控制在两行以内，不使用缩小字号的方式容纳长句。

## 连线标签规则

- 短连接线不要放长标签；距离较近时，连线 `value` 留空或只放“是 / 否 / 成功 / 失败”等短词。
- 协议、事件名和动作可以作为连线标签，原因说明和长描述优先写进节点或正文。
- 连线标签不得覆盖箭头主体，重点检查短横线、短竖线和菱形节点出口。
- 正文配图中的连线标签通常不超过 6 个中文字符。

## 画布选择

按图表内容选择画布，不强行把所有图都塞进同一比例：

| 场景 | pageWidth | pageHeight |
| --- | ---: | ---: |
| 正文横图 | `1000` | `700` |
| 正文竖图 | `760` | `1100` |
| 长流程图 | `760` | `1400` |

- 架构图、对比图和横向依赖关系优先使用正文横图。
- 流程图、状态图和移动端优先的内容使用正文竖图。
- 内容超过长流程画布时优先拆图，不继续增加高度或缩小字号。

## 基础模板

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2025-01-01T00:00:00.000Z" agent="article-diagram" version="24.0.0">
  <diagram name="Page-1" id="diagram-id">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1000" pageHeight="700" math="0" shadow="0" background="#FFFFFF">
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

图表主标题使用 `fontSize=30`，容器标题使用 `fontSize=20`，节点使用 `fontSize=20`，连线标签和旁注使用 `fontSize=16`。

文章上下文已经给出标题时，可以省略图内主标题。

```xml
<mxCell id="title" value="图表标题" style="text;html=0;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=30;fontStyle=1;fontColor=#111827;" vertex="1" parent="1">
  <mxGeometry x="300" y="24" width="400" height="46" as="geometry"/>
</mxCell>
```

## 节点样式模板

模板中的 `{类别填充色}`、`{类别边框色}` 和 `{类别文字色}` 对应视觉规范中的配色表。

### 通用节点模板

```xml
<mxCell id="node-id" value="节点名称" style="rounded=1;whiteSpace=wrap;html=0;arcSize=8;shadow=0;fillColor={类别填充色};strokeColor={类别边框色};strokeWidth=2;fontColor={类别文字色};fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=20;spacing=10;spacingTop=8;spacingBottom=8;" vertex="1" parent="1">
  <mxGeometry x="100" y="120" width="190" height="76" as="geometry"/>
</mxCell>
```

### 常见节点模板

```xml
<mxCell id="client-id" value="客户端" style="rounded=1;whiteSpace=wrap;html=0;arcSize=8;shadow=0;fillColor=#F8FAFC;strokeColor=#64748B;strokeWidth=2;fontColor=#1F2937;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=20;spacing=10;" vertex="1" parent="1">
  <mxGeometry x="56" y="120" width="190" height="76" as="geometry"/>
</mxCell>

<mxCell id="gateway-id" value="API 网关" style="rounded=1;whiteSpace=wrap;html=0;arcSize=8;shadow=0;fillColor=#EFF6FF;strokeColor=#3B82F6;strokeWidth=2;fontColor=#1E3A8A;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=20;spacing=10;" vertex="1" parent="1">
  <mxGeometry x="290" y="116" width="210" height="84" as="geometry"/>
</mxCell>

<mxCell id="service-id" value="用户服务" style="rounded=1;whiteSpace=wrap;html=0;arcSize=8;shadow=0;fillColor=#ECFDF5;strokeColor=#10B981;strokeWidth=2;fontColor=#065F46;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=20;spacing=10;" vertex="1" parent="1">
  <mxGeometry x="540" y="120" width="190" height="76" as="geometry"/>
</mxCell>

<mxCell id="worker-id" value="异步任务" style="rounded=1;whiteSpace=wrap;html=0;arcSize=8;shadow=0;fillColor=#FFF7ED;strokeColor=#F97316;strokeWidth=2;fontColor=#9A3412;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=20;spacing=10;" vertex="1" parent="1">
  <mxGeometry x="774" y="124" width="160" height="68" as="geometry"/>
</mxCell>

<mxCell id="db-id" value="MySQL 主库" style="shape=cylinder3;whiteSpace=wrap;html=0;boundedLbl=1;fillColor=#F5F3FF;strokeColor=#8B5CF6;strokeWidth=2;fontColor=#5B21B6;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=20;shadow=0;" vertex="1" parent="1">
  <mxGeometry x="540" y="260" width="180" height="84" as="geometry"/>
</mxCell>

<mxCell id="decision-id" value="条件?" style="rhombus;whiteSpace=wrap;html=0;fillColor=#EFF6FF;strokeColor=#3B82F6;strokeWidth=2;fontColor=#1E3A8A;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=20;shadow=0;" vertex="1" parent="1">
  <mxGeometry x="410" y="240" width="180" height="100" as="geometry"/>
</mxCell>

<mxCell id="group-id" value="服务层" style="swimlane;whiteSpace=wrap;html=0;rounded=1;arcSize=6;fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=2;fontColor=#1F2937;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=20;fontStyle=1;align=left;verticalAlign=top;spacing=14;spacingTop=10;shadow=0;" vertex="1" parent="1">
  <mxGeometry x="270" y="90" width="470" height="300" as="geometry"/>
</mxCell>
```

## 连线样式模板

### 默认同步请求

```xml
<mxCell id="edge-id" value="HTTP" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=0;endArrow=block;endFill=1;strokeWidth=2;strokeColor=#64748B;labelBackgroundColor=#FFFFFF;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=16;fontColor=#475569;" edge="1" source="source-id" target="target-id" parent="1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### 无标签连线

```xml
<mxCell id="edge-id" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=0;endArrow=block;endFill=1;strokeWidth=2;strokeColor=#64748B;" edge="1" source="source-id" target="target-id" parent="1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

### 异步消息

```xml
<mxCell id="edge-id" value="异步消息" style="edgeStyle=orthogonalEdgeStyle;rounded=1;orthogonalLoop=1;jettySize=auto;html=0;endArrow=block;endFill=1;dashed=1;strokeWidth=2;strokeColor=#D97706;labelBackgroundColor=#FFFFFF;fontFamily=PingFang SC, Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif;fontSize=16;fontColor=#92400E;" edge="1" source="source-id" target="target-id" parent="1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## 图表类型布局建议

### 流程图

- 默认使用 `760px` 宽的纵向画布，主干从上到下。
- 主节点水平居中，分支节点放在主干两侧。
- 分支判断使用菱形，出口只保留短标签。
- 单个流程超过 `10-12` 个步骤时，优先按阶段拆成两张图。

### 架构图

- 默认从左到右阅读，每行不超过 4 个主要角色。
- 推荐列坐标为 `56`、`290`、`524`、`758`，节点宽度按列数在 `160-190px` 之间选择。
- 先画层和容器，再画层内节点。
- 相同职责的节点放进同一容器；数据流和控制流使用不同线型或颜色。
- 结构超过 4 列时，优先改成分层布局或拆成“总体架构 + 核心链路”两张图。

### 时序图

- 参与者从左到右排布，消息按时间顺序自上而下。
- 单图参与者建议控制在 `4-6` 个。
- 横向过宽时拆分主链路和异常链路，不压缩参与者间距。
- 激活条只在确有必要时添加。

### ER 图

- 实体名清晰、字段简短，主键和外键关系明确。
- 公众号正文优先展示核心字段，完整字段表放到正文或附录。
- 复杂系统按子域拆图，不生成一张超宽 ER 图。

### 状态机图

- 状态是节点，事件是边，默认采用纵向或环形紧凑布局。
- 避免状态名和边标签都写成长句。
- 开始和结束状态要明显。

### 思维导图

- 从中心主题向外发散，第一层分支控制在 `4-6` 个。
- 分支较多时优先使用左右双向或纵向树形布局。
- 同层级节点保持视觉一致。

## 几何与密度规则

- 节点最小横向间距为 `56px`。
- 节点最小纵向间距为 `44px`。
- 同一行主节点不超过 4 个，单图主节点建议不超过 12 个。
- 连线标签放在边的中段，不能覆盖节点。
- 复杂图优先使用容器或拆成多个页面。
- 先放置内部节点，再根据节点范围确定容器尺寸。
- 不通过缩小字体解决拥挤问题。

## XML 注意事项

1. 每个 `mxCell` 必须有唯一 `id`。
2. 每条边必须有明确的 `source` 和 `target`。
3. 属性值中的特殊字符必须转义：`&amp;` `&lt;` `&gt;` `&quot;`。
4. XML 注释中不能使用 `--`。
5. 使用网格对齐，建议以 10px 为单位。
6. 需要精细控制连线时，用 `entryX/entryY` 指定入口位置。
7. 导出前检查画布边缘、容器边界、标签遮挡和节点重叠。
8. 以正文实际宽度或约 `375px` 宽度预览；文字过小时拆图，不降低规范字号。
