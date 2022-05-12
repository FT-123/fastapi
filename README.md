## Что заменить

    Задать свои параметры базы данных в ".env" и "docker-compose"

## Запуск

    docker compose up -d --build

## Миграции

    docker compose exec web alembic revision --autogenerate

## Swagger

    Windows - "127.0.0.1:8004/docs#/"
    Linux - "0.0.0.0:8004/docs#/"

## Redoc

    Windows - "127.0.0.1:8004/redoc#/"
    Linux - "0.0.0.0:8004/redoc#/"