# Django to do list project 
this project is for educational purposes

## Table of contents

- [Getting started](#getting-started)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Running the Application](#running-the-application)

## Getting started

1. Clone repository:

    ```bash
   git clone git@github.com:amirjonr/django-todo-list.git 
    ```
2. Navigate to project directory
    ```bash
   cd django-todo-list 
    ```

## Setting Up the Development Environment
1. Install Django via pip if not installed yet
    ```bash
   pip install django
    ```
2. Run migrations
   ```bash
   python manage.py migrate 
   ```
3. Create superuser
   ```bash 
   python manage.py createsuperuser
   ```

## Running the Application
1. Run server locally
   ```bash
   python manage.py runserver
   ```
2. Open your browser and navigate to <a href="http://localhost:8000/" target="_blank">this link</a> to see the application running.

---

## Thank you for using this app to learn django