# MO-02 · Журнал и карточка измерения

Направление: [Mobile · Dart и Flutter](../../README.md). Ориентир: 8–12 часов после изучения темы. Предыдущий шаг: MO-01.

## Цель

Собрать интерфейс из повторно используемых widgets.

## Входные материалы

[PulseLab](../../../../docs/01-project/pulselab.md), [fixtures](../../../../shared/fixtures/README.md), [контракты](../../../../shared/contracts/README.md). Используй свой код предыдущего задания; внешний backend/аккаунт/оборудование не являются зависимостью.

## Сделать

Построй журнал s001 на mock repository и карточку выбранной записи. Добавь фильтр kind, время в локальном представлении с подписью зоны и переключатель состояния mock: data/empty/error/loading.

Сначала опиши план из 3–5 шагов, затем реализуй минимальный путь и проверь ошибки. Если выбираешь другую библиотеку, объясни совместимость с технологией направления; замена основного стека требует согласования наставника.

## Критерии приёмки

- [ ] Список упорядочен по времени DESC и id ASC; выбранная карточка показывает unit и source.
- [ ] Все четыре состояния доступны для демонстрации и визуально различимы.
- [ ] При большом системном размере текста основные данные читаются; кнопки имеют понятные подписи.
- [ ] Widget-тест проверяет фильтр и переход в карточку; данные не хранятся внутри widgets.

## Сдать в личном публичном GitHub

- Код и осмысленные проверки поведения, ссылка на PR задачи.
- `docs/tasks/02-report.md`: реализация, команды, результаты проверок, решения и ограничения.
- `docs/tasks/02-answers.md`: ответы на [опросник](quiz.md).
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

Пример промпта: «Изучаю Mobile · Dart и Flutter для учебного MO-02. Объясни понятия, необходимые для цели “Собрать интерфейс из повторно используемых widgets.”, и дай маленькие отдельные упражнения. Не решай задание целиком. Сверяй API с моей версией и официальной документацией».
