# Контракты PulseLab

| Файл | Применение |
| --- | --- |
| `reading-input.schema.json` | Runtime-валидация входа при добавлении/импорте |
| `reading.schema.json` | Сохранённая запись с серверным id |
| `openapi.json` | REST, health и транспорт GraphQL |
| `schema.graphql` | SDL только для чтения данных |

JSON Schema — draft 2020-12; OpenAPI — 3.1.0. Проверка `format=date-time` должна быть включена в выбранном validator; pattern дополнительно запрещает timestamp без зоны. Значения NaN/Infinity не являются допустимыми JSON-числами. Числа в строках не преобразуются молча.

Schema проверяет структуру. Дополнительно приложение проверяет policy, from <= to, известные query fields и атомарную идемпотентность. `value >= 0` — только техническое правило упражнения, не клинический диапазон.

GraphQL String для kind/unit/date-time не отменяет runtime-проверку в общем сервисе. REST error statuses и GraphQL errors различаются по transport, но правила совпадают. X-Lab-Actor — fake identity только для локальных тестов. Read-only GraphQL ограничивает объём упражнения; это не описание возможностей ТМХ.

File endpoints и AI search/answer студенты описывают отдельным учебным расширением; не выдают их за основной контракт ТМХ. Общая спецификация поведения: [PulseLab](../../docs/01-project/pulselab.md).
