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

## Установка и запуск локально

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

## Настройка CI/CD и деплой на сервер

### 1. Установка

## Обновление и установка Docker

```
sudo apt update && sudo apt upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## Установка Docker Compose

```
sudo apt install docker-compose-plugin
```

## Добавление пользователя в группу docker

```
sudo usermod -aG docker $USER
```

## Настройка безопасности - firewall

```
sudo ufw allow 22    # SSH
sudo ufw allow 80    # HTTP
sudo ufw allow 443   # HTTPS
sudo ufw enable
```

## Автоматический деплой (CI/CD)

#### 1. Клонирование проекта

```
git clone https://github.com/mariazhiganova/Habit-Flow.git
cd Habit-Flow
```

#### 2. Добавление переменных окружения

```
nano .env # и добавить туда необходимые переменные (см. .env.example)
```

#### 5. Запуск и проверка статуса

```
docker-compose up -d
docker-compose ps
```

При каждом push в репозиторий автоматически:

#### Тестирование

    Запускаются все тесты Django

    Проверяется качество кода (flake8)

    Используется PostgreSQL + Redis

#### Деплой

    develop ветка → деплой на тестовый сервер

    main ветка → деплой на продакшен сервер

#### В Secrets в GitHub необходимо добавить:

    SECRET_KEY - секретный ключ Django

    SERVER_IP - IP вашего сервера

    SSH_PRIVATE_KEY - приватный SSH ключ

    DOCKERHUB_USERNAME и DOCKERHUB_TOKEN - для Docker Registry

## Доступ к приложению

Приложение доступно по IP: `158.160.202.72`

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
