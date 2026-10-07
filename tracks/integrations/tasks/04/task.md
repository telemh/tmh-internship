# IN-04 · REST и SOAP вымышленной МИС

Направление: [Интеграции · устройства, health-платформы и МИС](../../README.md). Ориентир: 8–12 часов после изучения темы. Предыдущий шаг: IN-03.

## Цель

Понять transport и безопасно преобразовать ответ.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Реализуй два fake HIS client: JSON REST и SOAP XML по shared fixtures. Оба дают учебные appointments. SOAP parser должен учитывать namespace и отвергать DTD/внешние entities; никаких сетевых обращений при разборе XML.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Оба клиента возвращают одинаковый canonical Appointment.
- [ ] SOAP Fault, HTTP 503, malformed XML и неизвестный subject дают явные ошибки.
- [ ] Перестановка namespace prefix не ломает mapping; непонятный status не превращается в confirmed.
- [ ] Тесты подтверждают отключённое разрешение внешних entities; выбранный parser и его настройки документированы.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/04-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/04-answers.md`: ответы на [опросник](quiz.md).
- Обновлённые README, зависимости/lock и AI-журнал; при UI — скриншот/видео на fixtures.

Оформление — по [инструкции сдачи](../../../../docs/00-start/submission.md). Готовые решения здесь не публикуются.

## Как изучать

Не нужно читать все руководства целиком: открой разделы по теме текущей задачи. Полный маршрут изучения указан во [вводной направления](../../README.md).

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

Пример промпта: «Изучаю Интеграции · устройства, health-платформы и МИС для учебного IN-04. Объясни понятия, необходимые для цели “Понять transport и безопасно преобразовать ответ.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
