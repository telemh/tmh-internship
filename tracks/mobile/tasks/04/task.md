# MO-04 · Добавление записи и очередь offline

Направление: [Mobile · Dart и Flutter](../../README.md). Ориентир: 8–10 часов после изучения темы. Предыдущий шаг: MO-03.

## Цель

Согласовать форму, локальное состояние и повторную отправку.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Сделай форму ReadingInput и локальную очередь pending/sent/failed. При отключённой mock-сети запись сохраняется как pending; после подключения отправляется с неизменным externalId. Backend имитирует 201, 200 и 409.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Валидация соответствует shared schema, нет клинических выводов.
- [ ] Два нажатия и повтор после потерянного ответа не создают вторую запись.
- [ ] Pending переживает перезапуск приложения в выбранном локальном хранилище.
- [ ] 409 отображается отдельно от временного сбоя; есть тест потерянного ответа после успешной записи.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/04-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/04-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю Mobile · Dart и Flutter для учебного MO-04. Объясни понятия, необходимые для цели “Согласовать форму, локальное состояние и повторную отправку.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
