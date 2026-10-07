# MO-05 · Эмулятор устройства и разрешений

Направление: [Mobile · Dart и Flutter](../../README.md). Ориентир: 8–12 часов после изучения темы. Предыдущий шаг: MO-04.

## Цель

Отработать события устройства без hardware и персональных данных.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Создай интерфейс источника и два fake adapter: BLE stream и health-platform. Воспроизведи connected/disconnected, permission granted/denied/revoked и повтор одного измерения. Используй только синтетические события.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Отказ или отзыв доступа прекращает импорт, но приложение остаётся работоспособным.
- [ ] Подписки закрываются; многократное открытие экрана не умножает listeners.
- [ ] Нормализация единиц и duplicate key соответствует учебной модели.
- [ ] Есть таблица сценариев и автоматические проверки отказа, отзыва и дубля; в README отдельно описано, что настоящая интеграция не реализована.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/05-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/05-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю Mobile · Dart и Flutter для учебного MO-05. Объясни понятия, необходимые для цели “Отработать события устройства без hardware и персональных данных.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
