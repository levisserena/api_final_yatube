# API_Yatube (version 2.0)

### О проекте.
Проект api_yatube позволяет вести форум, в котором пользователи могут оставлять сообщения, а так же комментарии к сообщениям других пользователей. Поддедрживается подписка пользователей друг на друга.
Особенностью проекта является возможность отправлять запросы посредством API.
___
### Информация об авторе.
Акчурин Лев Ливатович.<br>Студент курса Яндекс Практикума Python-разработчик плюс.
___
### При создании проекта использовалось:
- язык программирования Python версии 3.9.13;
- фреймворк Django версии 3.2.16
- фреймворк Django Rest Framework версии 3.12.4
- базы данных выполнены на Sqlite3
- API реализуется с использованием JSON
___
### Как развернуть проект.
Чтобы развернуть проект необходимо следующие:
- Форкнуть проект себе на репозиторий с:
```
https://github.com/levisserena/api_final_yatube
```

>*активная ссылка под этой кнопкой* -> [КНОПКА](https://github.com/levisserena/api_final_yatube)
- Клонировать репозиторий со своего GitHub и перейти в него в командной строке:

```
git clone https://github.com/<имя вашего акаунта>/api_yatube.git
```

```
cd yatube_api
```

- Создать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/bin/activate
```

- Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- Выполнить миграции:

```
python manage.py migrate
```
- Создать файл .env в корне проекта и указать в нём SECRET_KEY

```
SECRET_KEY = ...
```

- Запустить проект:

```
python manage.py runserver
```
___
### Эндпоинты.
- "jwt-create": "http://127.0.0.1:8000/api/v1/jwt/create/"
    - POST - получить токен пользователю;
- "jwt-refresh": "http://127.0.0.1:8000/api/v1/jwt/refresh/"
    - POST - обновление JWT-токена;
- "jwt-verify": "http://127.0.0.1:8000/api/v1/jwt/verify/"
    - POST - проверка JWT-токена;
- "posts": "http://127.0.0.1:8000/api/v1/posts/",
    - GET - список всех записей;
    - POST - создание записи;
- "posts": "http://127.0.0.1:8000/api/v1/posts/{post_id}/",
    - GET - отдельная запись;
    - PUT - изменение записи;
    - PATCH - частичное изменение записи;
    - DELETE - удаление записи;
- "comments": "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/",
    - GET - список всех комментариев отдельной записи;
    - POST – создание комментария к отдельной записи;
- "comments": "http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{comment_id}/",
    - GET - отдельный комментарий;
    - PUT - изменение комментария;
    - PATCH - частичное изменение комментария;
    - DELETE - удаление комментария;
- "groups": "http://127.0.0.1:8000/api/v1/groups/"
    - GET - список всех групп записей;
- "groups": "http://127.0.0.1:8000/api/v1/groups/{group_id}/"
    - GET - данные отдельной группы записей;
- "follow": "http://127.0.0.1:8000/api/v1/follow/"
    - GET - показывает на кого подписан пользователь;
    - POST – подписывает на указанного пользователя.
___
### Примеры запросов и ответов.
- Эндпоинт:
```
http://127.0.0.1:8000/api/v1/jwt/create/
```
- Запрос POST:
```JSON
{
    "username": "igor",
    "password": "1234567890asd"
}
```
- Ответ:
```JSON
{
  "refresh": "string",
  "access": "string"
}
```
---
- Эндпоинт:
```
http://127.0.0.1:8000/api/v1/posts/
```
- Запрос GET.
- Ответ:
```JSON
[
    {
        "id": 1,
        "text": "text_1",
        "pub_date": "2024-05-15T12:00:00.000000Z",
        "author": "root",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "text": "text_2",
        "pub_date": "2024-05-16T12:00:00.000000Z",
        "author": "root",
        "image": null,
        "group": null
    }
]
```
---
- Эндпоинт:
```
http://127.0.0.1:8000/api/v1/posts/
```
- Запрос POST:
```JSON
{
    "text": "text_text"
}
```
- Ответ:
```JSON
{
    "id": 3,
    "text": "text_text",
    "pub_date": "2024-05-17T12:00:00.000000Z",
    "author": "root",
    "image": null,
    "group": null
}
```
---
- Эндпоинт:
```
http://127.0.0.1:8000/api/v1/posts/6/comments/1/
```
- Запрос PATCH:
```JSON
{
    "text": "text_comment"
}
```
- Ответ:
```JSON
{
    "id": 1,
    "author": "igor",
    "post": 6,
    "text": "text_comment",
    "created": "2024-05-17T12:01:00.000000Z"
}
```
_Подробнее по эндпоинтам и по примерам запросов можно посмотрев в файле проекта_ `static/redoc.yaml`_, используя для этого, например [Seagger](https://editor.swagger.io/)._