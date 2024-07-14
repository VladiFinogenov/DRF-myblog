FROM python:3.11

# Устанавливаем переменные окружения
ENV DJANGO_SETTINGS_MODULE=myblog.settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt в контейнер
COPY requirements.txt /app

# Устанавливаем зависимости Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . /app

# Указываем, что контейнер будет слушать на порту 8000
EXPOSE 8000

# Создаем директорию для статических файлов
RUN mkdir -p /app/static

# ENTRYPOINT ["/app/entrypoint.sh"]
# # Выполняем миграции и загружаем фикстуры
# # RUN python manage.py makemigrations
# # RUN python manage.py migrate

CMD ['gunicorn', 'myblog.wsgi:application', '--bind', '0.0.0.0:8000']