# 我的 Codex Skills

这个仓库用于集中维护我自己使用的 Codex Skills。每个一级目录都是一个独立技能，可以单独安装、修改和迭代。

## 现有技能

| 技能 | 用途 |
| --- | --- |
| `article-diagram` | 根据文章或技术主题生成 draw.io 图表，支持流程图、架构图、时序图、ER 图、状态图和思维导图，并可按需导出为 PNG、SVG 或 PDF。 |
| `article-humanizer-zh` | 润色中文文章，识别并减少模板化的 AI 写作痕迹，同时保留原意、语气和必要的技术细节。 |

## 目录结构

```text
skills/
├─ article-diagram/
│  ├─ SKILL.md
│  ├─ agents/
│  │  └─ openai.yaml
│  └─ references/
│     ├─ export-and-files.md
│     ├─ style-spec.md
│     ├─ use-cases.md
│     └─ xml-and-layout.md
├─ article-humanizer-zh/
│  ├─ SKILL.md
│  └─ agents/
│     └─ openai.yaml
└─ README.md
```

各文件的职责：

- `SKILL.md`：技能入口，包含名称、触发条件、工作流程和输出要求。
- `agents/openai.yaml`：技能在 Codex 中显示的名称、简介和默认提示词。
- `references/`：按需读取的详细规范、示例或参考资料，避免让 `SKILL.md` 变得过长。

## 安装

将需要的技能目录复制或链接到 Codex 的 Skills 目录：

```text
$CODEX_HOME/skills/
```

如果没有设置 `CODEX_HOME`，通常可以使用用户目录下的 `.codex/skills/`。安装后重新启动 Codex 或开启新会话，让技能清单重新加载。

## 使用示例

在提示词中直接点名技能：

```text
使用 $article-diagram，把这篇技术文章整理成一份多页 draw.io 配图。
```

```text
使用 $article-humanizer-zh 润色下面的中文文章，保留原意和技术细节。
```

技能也支持根据任务描述自动触发，具体触发范围以各自的 `SKILL.md` 为准。

## 新增技能

今后添加自用技能时，遵循以下约定：

1. 一个技能使用一个独立目录，目录名与 `SKILL.md` 中的 `name` 保持一致。
2. `SKILL.md` 只保留触发条件、核心流程和验收规则；较长的规范或示例放进 `references/`。
3. 需要在 Codex 界面中展示名称和默认提示词时，添加 `agents/openai.yaml`。
4. 提交前用真实提示词试跑，确认技能能够正确触发，输出也符合预期。
5. 新增或删除技能后，同步更新本 README 中的技能列表和目录结构。

## 说明

这些技能主要服务于个人工作流，会随着实际使用持续调整。目前仓库不提供统一的构建或发布流程。
