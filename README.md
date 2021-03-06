# API Weather
An API built with Django/Django Rest Framework on the backend and ReactJs on the frontend to register the weather.

[![GitHub license](https://img.shields.io/github/license/marprezd/api-weather)](https://github.com/marprezd/api-weather/blob/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/marprezd/api-weather)](https://github.com/marprezd/api-weather/network)
[![GitHub stars](https://img.shields.io/github/stars/marprezd/api-weather)](https://github.com/marprezd/api-weather/stargazers)

## What does it cover?

- Python v3.9.1
- Django v3.1.5
- Djangorestframework v3.12.2
- PostgreSQL v12

## Repository structure

```
.
├── accounts
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── core_project
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── frontend
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── LICENSE.txt
├── manage.py
├── Pipfile
├── README.md
└── weather
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_auto_20210201_1702.py
    │   └── __init__.py
    ├── models.py
    ├── pagination.py
    ├── permissions.py
    ├── serializers.py
    ├── tests
    │   ├── factories.py
    │   ├── __init__.py
    │   └── tests.py
    ├── urls.py
    └── views.py

```

## Project task list

- [x] Create a virtual environment, install Django/Django Rest Framework, and create a Django Project.
- [x] Add Dockerfile and docker-compose.yml.
- [x] Setting databases.
- [x] Build models.
- [x] Run first migrations.
- [x] Run tests.
- [x] Set permissions policy.
- [x] Add pagination.
- [ ] Add authentication.
- [ ] Add filtering, searching, and ordering.


