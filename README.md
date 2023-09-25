# Репозиторий тестового задания на вакансию python-разработчик в компанию Пикассо.

## Данный проект находится по адресу 

````
https://task-picasso.ddns.net
````

### Адрес загрузки файла
````
https://task-picasso.ddns.net/api/v1/ulpad/
````

### Адрес списка загруженных файлов 
````
https://task-picasso.ddns.net/api/v1/ulpad/
````

### В данном проекте осуществлен следующий функционал:
- **Прием файлов типов: jpg, jpeg, png, gif, txt, text.**
- **Обратботка этих файлов, медиа файлы сжимаются до 200х100px, а текстовые переписываются.**
- **Выполнено покрытие тестами, но они покрывают не весь функционал.**
- **Проект развернут на VPS сервере, также подключен https-протокол, домен, статику раздает nginx и проксирует запросы.**
****

## Требования к окружению

- **Python - 3.9**
- **Django - 4.2.2**
- **DRF - 3.14.0**
- **PostgreSQL - 13.3**
- **Docker - 4.19**

## Установка и запуск

```bash
# Установка репозитория
git clone git@github.com:NikolayPetrow23/test_task_in_Picasso_Petrov_Nikolay.git
```

### Запустить данный проект можно двумя способами:
1. Запуск с помощью Docker
2. Запуск проекта в ручную


### Запуск проекта с помощью Docker:
```bash
# Билдим docker compose
docker compose build
```
```bash
# Запуск проекта с утановкой всех зависимостей, но нужно будет подождать!
docker compose up
```

### Запуск проекта в ручную:
```bash
# Установке зависимостей
pip install -r requirements.txt
```

```bash
# Поднятие базы данных с помощью Dokcer
docker run -p 5432:5432 --name "Имя вашей БД" -e POSTGRES_USER="Введите пользователя для БД" -e POSTGRES_PASSWORD="Введите пароль для БД" -e POSTGRES_DB="Имя вашей БД" -d postgres:13.3
```

```bash
# Переход в рабочую директорию
cd file_project
```

```bash
# Выполните миграции
python3 manage.py makemigrations
python3 manage.py migrate
```

```bash
# Установка фикстур
python3 manage.py load data api/fixtures/files.json
```

```bash
# Создание суперпользователя
python3 manage.py createsuperuser
```

```bash
# Запуск проекта
python3 manage.py runserver
```


## Автор
Николай Петров - [GitHub](https://github.com/NikolayPetrow23)
