# Интеграции · устройства, health-платформы и МИС

Интеграция переводит внешний контракт в модель приложения и контролирует ошибки на границе. REST и SOAP имеют разные формы обмена; webhook может повториться или прийти не по порядку; BLE и health-платформы требуют учитывать состояние подключения и разрешений.

Основной учебный язык — TypeScript/Bun, чтобы результат был близок к основному backend. Никаких партнёрских SDK, production-webhooks и реальных измерений. FHIR R4 — дополнительный обзор, не обязательный формат ТМХ.

## Где эти технологии применяются в ТМХ

1. ТМХ обменивается данными с МИС через REST/SOAP. В задании вымышленная МИС возвращает синтетический список записей.

2. Измерения поступают от устройств и облачных платформ. В задании два вымышленных провайдера имеют разные поля и единицы.

3. Webhook-интеграции требуют контроля повторов. В задании один eventId приходит несколько раз и после потерянного ответа.

4. Health-платформы дают пользователю управление разрешениями. В задании fake permission state останавливает импорт при отзыве.

Это общие функциональные примеры. Поля и endpoints упражнений относятся к PulseLab, не раскрывают реализацию продукта.

## Что изучить перед задачами

1. Adapter boundary, schema и нормализация времени/единиц.
2. Idempotency, retry/backoff, порядок событий и карантин ошибок.
3. Webhook raw body/HMAC на учебном ключе; никогда не копировать provider signature scheme.
4. SOAP/XML namespaces и безопасный parser; mapping внешних ID.

## Материалы

- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Bun docs](https://bun.com/docs)
- [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
- [JSON Schema](https://json-schema.org/learn/getting-started-step-by-step)
- [OpenAPI 3.1 specification](https://spec.openapis.org/oas/v3.1.0.html)
- [SOAP 1.1, W3C Note](https://www.w3.org/TR/2000/NOTE-SOAP-20000508/)
- [XML Namespaces, W3C](https://www.w3.org/TR/xml-names/)
- [Bluetooth technology overview](https://www.bluetooth.com/learn-about-bluetooth/tech-overview/)
- [Health Connect](https://developer.android.com/health-and-fitness/health-connect)
- [HealthKit](https://developer.apple.com/documentation/healthkit)
- [FHIR R4](https://www.hl7.org/fhir/R4/)

Сначала язык и базовая технология, затем соответствующий раздел API/ошибок/тестов. Версии зафиксируй в своём проекте; [статусы источников](../../docs/resources.md). Пример запроса AI: «Я студент с опытом [опыт]. Составь путь изучения тем выше за [часы], опираясь на официальные источники. Для каждой темы дай короткое объяснение и маленькое упражнение, которое не решает мою задачу целиком».

## Практика

Шесть задач по порядку; общий ориентир 46–70 часов плюс изучение незнакомых понятий. Каждая заканчивается публикацией артефактов в своём репозитории и опросником.

| Задача | Часы | После выполнения |
| --- | ---: | --- |
| [IN-01 · Два источника — одна модель](tasks/01/task.md) | 6–10 | [Опросник](tasks/01/quiz.md) |
| [IN-02 · Импорт с повторными событиями](tasks/02/task.md) | 8–12 | [Опросник](tasks/02/quiz.md) |
| [IN-03 · Учебный webhook-приёмник](tasks/03/task.md) | 8–12 | [Опросник](tasks/03/quiz.md) |
| [IN-04 · REST и SOAP вымышленной МИС](tasks/04/task.md) | 8–12 | [Опросник](tasks/04/quiz.md) |
| [IN-05 · Сбои, порядок и отзыв разрешения](tasks/05/task.md) | 8–12 | [Опросник](tasks/05/quiz.md) |
| [IN-06 · Контракт, тест-план и демо импорта](tasks/06/task.md) | 8–12 | [Опросник](tasks/06/quiz.md) |

Начни с [общих правил](../../SECURITY.md) и [инструкции сдачи](../../docs/00-start/submission.md). [Оценивание](../../assessment/rubric.md) открыто заранее. Если нет нужного hardware/OS, обязательный маршрут выполняется через указанные mocks.
