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
2. Покрытие тестами:
Name                                                             Stmts   Miss  Cover
------------------------------------------------------------------------------------
config\__init__.py                                                   0      0   100%
config\asgi.py                                                       4      4     0%
config\settings.py                                                  25      0   100%
config\urls.py                                                       3      0   100%
config\wsgi.py                                                       4      4     0%
manage.py                                                           11      2    82%
materials\__init__.py                                                0      0   100%
materials\admin.py                                                  10      0   100%
materials\apps.py                                                    4      0   100%
materials\migrations\0001_initial.py                                 5      0   100%
materials\migrations\0002_lesson_course.py                           5      0   100%
materials\migrations\0003_course_owner_lesson_owner.py               6      0   100%
materials\migrations\0004_subscription.py                            6      0   100%
materials\migrations\__init__.py                                     0      0   100%
materials\models.py                                                 31      3    90%
materials\paginators.py                                              5      0   100%
materials\serializers.py                                            28      1    96%
materials\tests.py                                                  78      0   100%
materials\urls.py                                                    8      0   100%
materials\validators.py                                              5      1    80%
materials\views.py                                                  63     10    84%
users\__init__.py                                                    0      0   100%
users\admin.py                                                       9      0   100%
users\apps.py                                                        4      0   100%
users\management\__init__.py                                         0      0   100%
users\management\commands\__init__.py                                0      0   100%
users\management\commands\create_group_moderator.py                 12     12     0%
users\management\commands\create_payment.py                         19     19     0%
users\management\commands\csu.py                                    10     10     0%
users\migrations\0001_initial.py                                     7      0   100%
users\migrations\0002_payment.py                                     6      0   100%
users\migrations\0003_alter_payment_payment_course_and_more.py       5      0   100%
users\migrations\__init__.py                                         0      0   100%
users\models.py                                                     31      2    94%
users\permissions.py                                                 7      0   100%
users\serializers.py                                                10      0   100%
users\tests.py                                                       1      0   100%
users\urls.py                                                        7      0   100%
users\views.py                                                      29      3    90%
------------------------------------------------------------------------------------
TOTAL                                                              458     71    84%
