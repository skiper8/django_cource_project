## Курсовая 6. Основы веб-разработки на Django

### 1. Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:
    Команда для Windows:
        1- python -m venv venv
        2- venv\Scripts\activate
        3- pip install -r requirement.txt

    Команда для Unix:
        1- python3 -m venv venv
        2- source venv/bin/activate 
        3- pip install -r requirement.txt

### 2. Для запуска celery:
        1- celery -A config worker -l info  

### 3. Для запуска redis:
    Redis официально не поддерживается в Windows: 
        1- Установите WSL2, Ubuntu. Подробности смотрите тут https://redis.io/docs/getting-started/installation/install-redis-on-windows/
        2- sudo apt-get update
        3- sudo service redis-server start
        4- redis-cli
        5- ping
        
        Ответом от сервиса должно быть PONG. Это означает что Redis подключен

    Команда для Unix:
        1- redis-cli

### 4. Для заполнения моделей данными необходимо выполнить следующую команду: 
    Команда для Windows:
        1- python manage.py add_blog
        2- python manage.py add_mailing

    Команда для Unix:
        1- python3 manage.py add_blog
        2- python3 manage.py add_mailing

### 5. Для работы с переменными окружениями необходимо заполнить файл
    - .env

### 6. Для создания администратора (createsuperuser)
    - заполните поля email, PASSWORD. users/management/commands/csu.py
    Команда для Windows
    1- python manage.py csu

    Команда для Unix
    - python3 manage.py csu
### 7. Для запуска приложения: 
    Команда для Windows:
    - python manage.py runserver

    Команда для Unix:
    - python3 manage.py runserver

### 8. Для отправки рассылки из командной строки: 
    Команда для Windows:
    - python manage.py sendmessage N, где N - это PK рассылки (узнать PK рассылки можно в админке)

    Команда для Unix:    
    - python3 manage.py sendmessage N, где N - это PK рассылки (узнать PK рассылки можно в админке)