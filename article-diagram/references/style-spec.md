# Draw.io 视觉规范

本文件定义 article-diagram 的统一视觉风格：Editorial Clearline。

风格以上游 drawio-chart 的原版视觉语法为基础，只做轻量个性化：保留实色节点、白色文字、无边框、轻阴影、紧凑字号和正交连线，仅调整配色、中文字体栈与背景色。

## 基础视觉语法

以下特征必须保留：

- 节点使用高对比实色填充，主要节点使用白色文字
- 节点默认无边框，并开启轻阴影
- 容器比节点更轻，优先使用透明背景和虚线边界
- 节点、容器和连线保持紧凑，不为了填满画布而放大
- 布局由内容关系决定，不把所有页面套进同一种卡片模板

## 轻量个性化边界

默认只允许通过以下方式形成区别：

- 使用本文件定义的微调配色
- 优先使用适合中文的系统字体栈
- 使用 `#F7F9FC` 作为画布和连线标签背景
- 同一篇文章保持一致的节点语义和间距

除非用户明确要求，不要默认加入编号徽章、顶部彩条、总结条、仪表盘卡片、装饰性副标题或作者水印。不要把原版实色节点改成浅色填充加深色描边。

## 配色系统

### 核心语义类别

| 语义类别 | 填充色 | 文字色 | 边框色 | 用途 |
| --- | --- | --- | --- | --- |
| **Gateway / Entry** | `#0B6170` | `#FFFFFF` | `none` | API 网关、入口、执行循环 |
| **Business Service** | `#D9864F` | `#FFFFFF` | `none` | 核心业务服务、工具执行 |
| **Infrastructure Service** | `#6F5CC2` | `#FFFFFF` | `none` | 记忆、认证、日志、监控 |
| **Client / Frontend** | `#1889A2` | `#FFFFFF` | `none` | 用户、前端、调用方 |
| **External / 3rd Party** | `#64748B` | `#FFFFFF` | `none` | 外部 API、第三方服务 |

### 数据存储类别

| 语义类别 | 填充色 | 文字色 | 边框色 | 用途 |
| --- | --- | --- | --- | --- |
| **Primary DB** | `#D9864F` | `#FFFFFF` | `none` | 主数据库、核心存储 |
| **Replica DB** | `#D8B77C` | `#2D3748` | `none` | 从库、只读副本 |
| **Cache / Queue** | `#44978C` | `#FFFFFF` | `none` | Redis、Kafka、RabbitMQ |
| **Search Engine** | `#1889A2` | `#FFFFFF` | `none` | Elasticsearch 等搜索引擎 |
| **Object Storage** | `#6F5CC2` | `#FFFFFF` | `none` | S3、OSS 等对象存储 |

### 状态类别

| 语义类别 | 填充色 | 文字色 | 边框色 | 用途 |
| --- | --- | --- | --- | --- |
| **Success / Status** | `#44978C` | `#FFFFFF` | `none` | 正常流、成功状态 |
| **Alert / Danger** | `#DC2626` | `#FFFFFF` | `none` | 异常流、错误状态 |
| **Warning / Retry** | `#D9864F` | `#FFFFFF` | `none` | 重试、降级、等待确认 |
| **Info / Neutral** | `#94A3B8` | `#FFFFFF` | `none` | 中性状态、待处理 |

### 容器类别

| 语义类别 | 填充色 | 文字色 | 边框色 | 用途 |
| --- | --- | --- | --- | --- |
| **Group / Infra** | `none` | `#2D3748` | `#0B6170` | 容器、网络、分组区域 |
| **Network Zone** | `#F7F9FC` | `#2D3748` | `#E2E8F0` | 网络分区、安全域 |

## 全局常量

| 属性 | 值 | 说明 |
| --- | --- | --- |
| **Background** | `#F7F9FC` | 稍暖的浅灰文章背景 |
| **Font Family** | `system-ui, -apple-system, PingFang SC, Microsoft YaHei, Noto Sans CJK SC, sans-serif` | 中文系统字体栈 |
| **Font Size (Title)** | `20` | 图表主标题 |
| **Font Size (Node)** | `15` | 普通节点、容器标题 |
| **Font Size (Edge Label)** | `15` | 连线标签 |
| **Shape** | `rounded=1` | 矩形开启圆角 |
| **Edge Style** | `edgeStyle=orthogonalEdgeStyle;rounded=0` | 直角正交连线 |
| **Edge Width** | `strokeWidth=2` | 默认连线粗细 |
| **Edge Color** | `#94A3B8` | 默认箭头色 |
| **Label BG** | `labelBackgroundColor=#F7F9FC` | 连线标签与画布一致 |

## 高级设置

| 设置 | 值 | 说明 |
| --- | --- | --- |
| **Shadow** | `shadow=1` | 保留原版轻阴影效果 |
| **Gradient** | 禁用 | 使用稳定实色 |
| **Sketch Mode** | 禁用 | 除非用户明确要求草图风格 |

## 使用建议

- 一张图通常使用中性色加 `2-3` 种语义色。
- 同一语义节点使用同一种颜色，不随机配色。
- 容器保持轻量，核心节点保持明确。
- 文字较多时拆分节点或页面，不放大节点制造空洞感。
- 多页文章配图可以使用不同构图，但视觉常量必须一致。
