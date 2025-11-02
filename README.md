# HabitFlow - Трекер полезных привычек

Система для создания и отслеживания полезных привычек с автоматическими напоминаниями в Telegram.

## Возможности

- Создание полезных и приятных привычек
- Автоматические напоминания в Telegram
- Гибкая периодичность выполнения (ежедневно, еженедельно)
- Связывание полезных привычек с приятными (система вознаграждений)
- Публикация привычек для других пользователей
- REST API для интеграции

## Технологии

- **Backend**: Django 4.2 + Django REST Framework
- **Database**: PostgreSQL
- **Task Queue**: Celery + Redis
- **Notifications**: Telegram Bot API
- **Auth**: JWT-аутентификация

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/mariazhiganova/Habit-Flow.git
```

### 2. Установите зависимости

```commandline
poetry install
poetry shell
```

### 3. Переменные окружения

Создайте файл .env на основе .env.example

### 4. Запуск

```
python manage.py migrate
python manage.py runserver
```

### 5. Celery (в отдельном терминале)

```
celery -A config worker -l INFO
celery -A config beat -l INFO
```

## Документация

Вы можете увидеть документацию API, перейдя по URL-адресу

Для Swagger:

```
http://localhost:8000/swagger/
```

Для Redoc:

```
http://localhost:8000/redoc/
```

## Автор

**Мария Жиганова** - Backend Developer (Python)

```
GitHub - https://github.com/mariazhiganova
```
