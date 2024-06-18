## СТЕК

- Django
- DRF
- PostgreSQL


## **Запуск проекта**


> docker-compose up -d --build

### Создать суперпользователя и тестовые данные

> docker-compose exec app ./manage.py createsuperuser

> docker-compose exec app ./manage.py create_test_data


### API

- http://0.0.0.0:8000/api/departments/ - список всех отделов
- http://0.0.0.0:8000/api/departments/{department_id}/employees/ - список сотрудников отдела



