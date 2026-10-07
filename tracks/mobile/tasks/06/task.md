# MO-06 · Завершённое демо и проверка качества

Направление: [Mobile · Dart и Flutter](../../README.md). Ориентир: 8–12 часов после изучения темы. Предыдущий шаг: MO-05.

## Цель

Довести приложение до проверяемого результата.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Объедини предыдущие задачи. Добавь fake notification с безопасным переходом в Reading и финальный сценарий: просмотр → offline-ввод → reconnect → повтор → карточка. Оформи CI, инструкции и короткое видео.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] flutter analyze и flutter test проходят; команды и SDK зафиксированы.
- [ ] Уведомление с неизвестным id не ломает навигацию; чувствительный payload не используется.
- [ ] Сценарий повторяется из чистого clone по README без backend другого студента.
- [ ] Есть список известных ограничений и журнал исправлений после review; наставник может попросить добавить новый фильтр.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/06-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/06-answers.md`: ответы на [опросник](quiz.md).
- Обновлённые README, зависимости/lock и AI-журнал; при UI — скриншот/видео на fixtures.

Оформление — по [инструкции сдачи](../../../../docs/00-start/submission.md). Готовые решения здесь не публикуются.

## Как изучать

Не нужно читать все руководства целиком: открой разделы по теме текущей задачи. Полный маршрут изучения указан во [вводной направления](../../README.md).

- [Dart language](https://dart.dev/language)
- [Learn Flutter](https://docs.flutter.dev/learn)
- [Flutter architecture](https://docs.flutter.dev/app-architecture)
- [Flutter testing](https://docs.flutter.dev/testing/overview)
- [Bluetooth technology overview](https://www.bluetooth.com/learn-about-bluetooth/tech-overview/)
- [Health Connect](https://developer.android.com/health-and-fitness/health-connect)
- [HealthKit](https://developer.apple.com/documentation/healthkit)
- [Firebase Cloud Messaging](https://firebase.google.com/docs/cloud-messaging)

Пример промпта: «Изучаю Mobile · Dart и Flutter для учебного MO-06. Объясни понятия, необходимые для цели “Довести приложение до проверяемого результата.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
