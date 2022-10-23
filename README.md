# API для YaMDb

В этом учебном проекте **"API для YaMDb"** создан *REST API - сервис* для проекта YaMDb на основе классов предоставляемых библиотекой **Django REST Framework**.
Проект **YaMDb** собирает отзывы пользователей на различные произведения.
Аутентификация выпоняется по **JWT-токену**.

### Технологии:

Python 3.7
Django 2.2.16
Docker 20.10
gunicorn
PostgreSQ
nginx

### Как запустить проект в контейнерах:

Шаблон наполнения .env файла:

```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=xxxxxx # имя базы данных
POSTGRES_USER=xxxxxx # логин для подключения к базе данных
POSTGRES_PASSWORD=xxxxxx # пароль для подключения к БД (установите свой)
DB_HOST=xxxxxx # название сервиса (контейнера)
DB_PORT=xxxxxx # порт для подключения к БД
```

Инструкции по развертыванию проекта docker-compose расположены в каталоге infra_sp2/infra/
Развернуть проект командой:

```
docker-compose up
```

В контейнере web нужно выполнить миграции, создать суперпользователя и собрать статику:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

Через админку по адресу http://localhost/admin/ авторизируемся как суперпользователь,
устанавливаем начальные записи для объектов (жанры, категории и т.д.).

### Как запустить проект в dev-режиме:

Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/Vladislav-76/api_yamdb.git
```

```
cd api_api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейти в корневую папку проекта:

```
cd api_yamdb
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Алгоритм регистрации пользователей
1. Пользователь отправляет POST-запрос на добавление нового пользователя с параметрами email и username на эндпоинт ```/api/v1/auth/signup/```.
2. YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email.
3. Пользователь отправляет POST-запрос с параметрами username и confirmation_code на эндпоинт ```/api/v1/auth/token/```, в ответе на запрос ему приходит token (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на эндпоинт ```/api/v1/users/me/``` и заполняет поля в своём профайле (описание полей — в документации).

### Пользовательские роли

- Аноним — может просматривать описания произведений, читать отзывы и комментарии.
- Аутентифицированный пользователь (user) — может, как и Аноним, читать всё, дополнительно он может публиковать отзывы и ставить оценку произведениям (фильмам/книгам/песенкам), может комментировать чужие отзывы; может редактировать и удалять свои отзывы и комментарии. Эта роль присваивается по умолчанию каждому новому пользователю.
- Модератор (moderator) — те же права, что и у Аутентифицированного пользователя плюс право удалять любые отзывы и комментарии.
- Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- Суперюзер Django — обладет правами администратора (admin)


После запуска проекта, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API **YaMDb **. В документации описано, как работает API. Документация представлена в формате **Redoc**.
Ссылки для **Browsable API**:

http://127.0.0.1:8000/api/v1/auth/signup/
http://127.0.0.1:8000/api/v1/auth/token/
http://127.0.0.1:8000/api/v1/users/
http://127.0.0.1:8000/api/v1/genres/
http://127.0.0.1:8000/api/v1/categories/
http://127.0.0.1:8000/api/v1/titles/

### Некоторые примеры запросов к API:

**POST** /api/v1/auth/signup/

*Request samples*
```
{
    "email": "string",
    "username": "string"
}
```
*Response samples*
```
{
    "email": "string",
    "username": "string"
}
```

**GET** /api/v1/titles/

*Response samples*
```
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results":
        [
            {
                "id": 0,
                "name": "string",
                "year": 0,
                "rating": 0,
                "description": "string",
                "genre": [],
                "category": {}
            }
        ]
    }
]
```

**POST** /api/v1/titles/{title_id}/reviews/{review_id}/comments/

*Request samples*
```
{
    "text": "string"
}
```
*Response samples*
```
{
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
}
```
