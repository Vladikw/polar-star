# Полярная звезда

Информационная система бронирования и учёта номеров для сети мини-отелей: единая база бронирований, защита от двойных броней, выбор номера на плане этажа, отчёты по загрузке и выручке.

**Стек:** React + TypeScript, FastAPI, PostgreSQL, Docker Compose, Nginx, Linux.

## Быстрый старт

```bash
git clone <АДРЕС_РЕПОЗИТОРИЯ>
cd polar-star
cp backend/.env.example backend/.env    # задайте SECRET_KEY и пароль БД
docker compose up -d --build
```

Сайт: http://localhost. Документация API: http://localhost:8000/docs.

Остановить: `docker compose down` (с удалением данных БД: `docker compose down -v`).

## Настройки (backend/.env)

```env
DATABASE_URL=postgresql+psycopg://polar:CHANGE_ME@db:5432/polar
SECRET_KEY=CHANGE_ME_LONG_RANDOM_STRING
```

Файл `.env` в репозиторий не добавляется.

## Первый вход

Тестовые данные: `docker compose exec backend python -m app.db.seed`

<!-- ЗАПОЛНИТЬ: логины и пароли тестовых пользователей (sysadmin, admin, director, guest) -->

## Установка на сервер

- Linux (Ubuntu 22.04 / 24.04), 4 ядра, 8 ГБ ОЗУ, 100 ГБ диска, сервер на территории РФ.
- Установить Docker: `curl -fsSL https://get.docker.com | sudo sh`
- Открыть только порты 80 и 443 (порт PostgreSQL наружу не открывать).
- Выполнить шаги из «Быстрого старта». PostgreSQL запускается в контейнере, отдельно её ставить не нужно.
- Первая учётная запись администратора: <!-- ЗАПОЛНИТЬ: как создаётся -->
- Платёжный шлюз: в текущей версии оплата работает как заглушка, настройка не требуется.

## Резервное копирование

Копия базы:

```bash
docker compose exec -T db pg_dump -U polar polar > backup_$(date +%F).sql
```

Восстановление:

```bash
cat backup_ДАТА.sql | docker compose exec -T db psql -U polar polar
```

Для ежедневной копии добавьте эту команду в `cron`.
