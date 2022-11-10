# Expense_Accounting_Manager

## Менеджер учёта расходов

> Сервис для учёта расходов пользователя. Реализована система транзакций с помощью которых происходит списание, начисление баланса пользователя. Чтобы грамотно рассчитать свой бюджет каждый день на почту приходит статистика. Для того чтобы узнать куда вы тратите больше всего денег сделаны категории, которые можно выбрать из базовых или добавить свои.

## Технологии проекта

- Python — высокоуровневый язык программирования.
- PostgreSQL — объектно-реляционная система управления базами данных.
- DRF - фреймворк для написания API.
- Для планировки отправки писем использован Celery и брокер RabbitMQ
- Для автоматизации развёртывания ПО был использован Docker.

## Как запустить приложение в контейнере:

В директории создайте файл .env с переменными окружения для работы с базой данных:

```
SECRET_KEY=#секретный ключ django
EMAIL_HOST_USER=#ваш gmail с которого отправляется почта
EMAIL_HOST_PASSWORD=#пароль для вашего gmail аккаунта
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=#имя базы данных
POSTGRES_USER=#логин для подключения к базе данных
POSTGRES_PASSWORD=# пароль для подключения к БД
DB_HOST=название сервиса (контейнера)
DB_PORT=порт для подключения к БД
```

Выполнить команду:
```
docker-compose up
```
Произвести миграции:
```
docker-compose exec expense_accounting_manager python manage.py migrate
```
Загрузить категории в базу данных:
```
docker-compose exec expense_accounting_manager python manage.py csv_import
```
#### Опционально:
Запуск celery для отправки сообщений на почту:
```
docker-compose exec expense_accounting_manager celery -A expense_accounting_manager worker -l info
docker-compose exec expense_accounting_manager celery -A expense_accounting_manager beat -l info
```

## Примеры запросов к API

Регистрация пользователя.

```
POST /api/signup/
```

REQUEST:

```
{
    "username": "admin",
    "email": "1@mail.ru",
    "password": "1111"
}
```

Создание новой транзакции

```
POST /api/transaction/
```

REQUEST:

```
{
    "amount": "100",
    "category": "5",
    "organization": "1",
    "user": "3"
}
```