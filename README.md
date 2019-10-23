# Домашнее задание 23
## Настроить логирование ошибок в Sentry.

В REST-API бэкенда для сайта с курсами добавлена интеграция с Sentry. Для тестирования логирования добавлен
эндпойнт 'sentry-debug/' (т.е. обращаться к нему при тестировании на локальной машине нужно по адресу
http://127.0.0.1:8000/educ_api/sentry-debug/).

Ссылка на исключение: https://sentry.io/share/issue/c86f0be9a28946e9adf8bf43b207d67b/

## Использование
### Подготовка к работе
Перед запуском веб-приложения необходимо установить необходимые библиотеки и восстановить базу данных.
Для этого требуется из корневого каталога проекта выполнить команды:

    pip install -r requirements.txt
	python manage.py migrate
	python manage.py loaddata data.json

### Запуск
В корневом каталоге проекта (где лежит manage.py) выполнить команду:

	python manage.py runserver