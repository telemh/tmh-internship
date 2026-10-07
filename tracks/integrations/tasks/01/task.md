# IN-01 · Два источника — одна модель

Направление: [Интеграции · устройства, health-платформы и МИС](../../README.md). Ориентир: 6–10 часов после изучения темы. Предыдущий шаг: Вводная диагностика и подготовка среды.

## Цель

Научиться явному mapping и контролю качества входа.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Прочитай vendor-a.json и vendor-b.json. Сделай чистые adapter-функции для ReadingInput. Vendor A передаёт pulse в bpm, Vendor B — glucose в mg/dL; для упражнения используй mg/dL / 18.0182 и округление до 3 знаков. Удалять исходный unit из отчёта о mapping нельзя.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Все валидные элементы нормализуются; externalId и source стабильно сохраняются.
- [ ] Unix milliseconds и RFC3339 корректно переводятся в UTC.
- [ ] Ошибка unit, неизвестный subject mapping или missing field не сохраняется как валидная запись.
- [ ] Unit-тесты проверяют конверсию, timestamp, некорректный вход и mapping; формула обозначена как правило учебного адаптера.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/01-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/01-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю Интеграции · устройства, health-платформы и МИС для учебного IN-01. Объясни понятия, необходимые для цели “Научиться явному mapping и контролю качества входа.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
