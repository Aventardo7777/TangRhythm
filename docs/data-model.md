# Data Model

Core entities:

- Poem
- Author
- Dynasty
- Location
- HistoricalEvent
- Theme
- Emotion
- Imagery
- LiteraryDevice
- FamousLine
- KnowledgePoint
- Question
- LearningRecord
- User

核心关系：

`Author -> writes -> Poem`

`Poem -> contains -> Imagery`

`Poem -> expresses -> Emotion`

`Poem -> has_theme -> Theme`

`Poem -> mentions -> Location`

`Poem -> related_to -> HistoricalEvent`

`Poem -> similar_to -> Poem`
