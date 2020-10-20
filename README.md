# acits_test_django - тестовое задание на использование фреймворка django

## Задание:
### Нужно создать веб-приложение для управления базой данных животных.
База данных:  PostgreSQL.
Параметры животного: кличка, возраст, дата прибытия в приют, вес, рост, особые приметы (строка).

### Создать API:
- вывода на страницу всех животных (со строкой особых примет)
- создания животного
- редактирования/удаления животного
на базе Django Rest Framework, где вместо рендеринга HTML-страниц, бэкенд возвращает данные в JSON формате.

### Создать систему разделения прав:
- admin - администратор, имеет права: создание животного, редактирование, чтение, мягкое удаление
- user - приют, имеет права: создание, редактирование, чтение
- guest - гость, имеет право только на чтение (для презентации в приютах)
Каждый авторизованный пользователь может видеть животных только из своего приюта. То есть, пользователь привязан к приюту.

### Осуществить функции:
- добавление нового животного
- мягкое удаление животного из базы

## Описание приложений проекта:
### pets:
- основная логика приложения для управления БД животных (Django 3.1.2)
- система доступов работает на основании прав пользователя/группы в панели администрирования

### pets_rest_api:
- CRUD api для приложения pets
- методы требуют авторизацию (права доступа пользовтеля так же проверяются)
- pets.postman_collection.json - коллекция методов pets_rest_api для POSTMAN
       
## Настройки:
1. [создайте и подключите бд Postgresql]
1. Создайте и активируйте виртуальное окружение: 
`virtualenv venv 
source venv/bin/activate`

1. Установите пакеты из requirements.txt: 
`pip install -p requirements.txt`

1. Сделайте миграцию приложения:
 `./acits_test_django/python manage.py makemigration`
`./acits_test_django/python manage.py migrate`

1. Создайте супер-пользователя
`./acits_test_django/python manage.py createsuperuser`

## Запуск приложения
`./acits_test_django/python manage.py runserver`

## Настройки запущенного приложения

1. создаем группы пользователей:
`http://127.0.0.1:8000/admin/auth/group/`
Admins (даем права доступа в pets: can add, can change, can delete, can view )
Users (даем права доступа в pets: can add, can change, can view )
Guests (даем права доступа в pets: can view )

1. создаем нужное количество пользователей и добавляем их в группы:
`http://127.0.0.1:8000/admin/auth/user/`

1. создаем приюты:
`http://127.0.0.1:8000/admin/pets/shelter/`

1. создаем профайлы пользователей:
`http://127.0.0.1:8000/admin/pets/profile/`

[создайте и подключите бд Postgresql]: (https://djbook.ru/examples/77/)