# LMS-система

## Описание:

Платформа для онлайн-обучения, в которой каждый желающий может размещать свои полезные материалы или курсы. 

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:DadashovaYuliya/DRG_Module_8.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Настройте файл .env:
```
Из шаблона .env.sample создайте файл .env:

Для работы с django укажите Ваш секретный ключ и статус debug
SECRET_KEY=
DEBUG=

Для проекта используется база данных PostgreSQL. Укажите ваши параметры, предварительно создав пустую БД
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
POSTGRES_PORT=
```
## Приложения

1. Приложение materials, в котором описаны модели Course и Lesson. 
2. Приложение users, в котором описаны модели User и Payment.

## Контроллеры

1. Для модели Course создан контроллер на основе viewsets с сериализатором CourseSerializer.
2. Для модели Lesson создан контроллер на основе generics с сериализатором LessonSerializer.
3. Для модели Payment создан контроллер на основе generics с сериализатором PaymentSerializer.

## Маршрутизация:

1. Для представлений Course, Lesson, Payment настроена соответствующая маршрутизация.

## Тестирование:

1. Для тестирования заполнения БД по модели Payment можно использовать кастомную команду: python manage.py create_payment