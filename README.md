# HireFlow

Backend API для платформы по подбору персонала, разработанный на FastAPI.

## Стек технологий

- Python 3.14
- FastAPI
- PostgreSQL
- SQLAlchemy 2.0
- Alembic
- Redis
- Celery
- JWT Authentication
- Pydantic v2
- Docker
- Pytest

## Структура проекта

```
hireflow/
│
├── app/
│   ├── api/
│   ├── config/
│   ├── core/
│   ├── database/
│   ├── middlewares/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── tests/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Запуск проекта

Создать виртуальное окружение:

```bash
python -m venv venv
```

Активировать:

```bash
source venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Запустить сервер:

```bash
uvicorn app.main:app --reload
```

После запуска документация будет доступна по адресу:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Статус проекта

Проект находится в активной разработке.

Планируется реализация:

- авторизации пользователей;
- работы с PostgreSQL;
- миграций Alembic;
- JWT-аутентификации;
- системы вакансий;
- откликов кандидатов;
- Docker-конфигурации;
- тестирования.

---

Разработка ведется в учебных целях.