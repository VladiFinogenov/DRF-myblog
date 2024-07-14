# Blog API Backend

`REST API для блога, созданный с использованием Django Rest Framework.`

## Запуск проекта из открытого репозитория и распаковка контейнера

## Шаг 1: Клонирование репозитория

`Сначала клонируйте репозиторий на ваш локальный компьютер. Для этого выполните следующую команду:`

```bash
git clone https://github.com/VladiFinogenov/DRF-myblog.git
```

## Шаг 2: Переход в директорию проекта

```bash
cd DRF-myblog
```

## Шаг 3: Настройка переменных окружения

`Создайте файл .env в корневой директории проекта и добавьте в него необходимые переменные окружения. Для этого скопируйте и заполните из empty_env переменные. Пример:`
```bash
DEBUG = True
SECRET_KEY = 'django-insecure-xxxxxxxxxxxx'
DJANGO_ALLOWED_HOSTS = '127.0.0.1'
CSRF_TRUSTED_ORIGINS = 'http://127.0.0.1'
INTERNAL_IPS = '127.0.0.1'

POSTGRES_USER = 'blog'
POSTGRES_PASSWORD = 'new_password'
POSTGRES_DB = 'your_database'
```
## Шаг 4: Сборка и запуск контейнеров Docker

`Соберите и запустите контейнеры Docker с помощью docker-compose:`
```bash
docker compose up --build
```
`Эта команда соберет образы Docker и запустит контейнеры в соответствии с конфигурацией, указанной в файле docker-compose.yml.`

`❗ В контейнере автоматически запустятся миграции и сборка статики`

## Шаг 5: Создание суперпользователя

`Создайте суперпользователя для доступа к административной панели:`
`Для этого откройте второй терминал и введите команду:`
```bash
docker compose run web python manage.py createsuperuser
```

# RESTAPI Docs
`Документация по пользовательскому интерфейсу Swagger:` http://127.0.0.1:8000/api/docs/

`При работе с API в браузере вы можете войти в систему по ссылке` http://127.0.0.1:8000/api-auth/login/