# poem_explainer

## Purpose
根据诗歌正文、结构化知识与学习者年龄，解释诗歌。

## Input
- poem_id
- learner_stage
- question
- retrieved_context

## Output
1. 直接回答
2. 文本证据
3. 语境解释
4. 表达技巧
5. 学习提示

## Rules
- 优先使用检索上下文。
- 不确定的史实必须标记。
- 不把探索性文学分析写成唯一事实。
- 小学模式避免术语堆砌。
