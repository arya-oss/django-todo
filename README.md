## ToDos Web Application

### Overview and Features

> Simple ToDo work managing web Application for different Users.

* __Login and Registration__
* __Update and Manage Profile__
* __Manage ToDos (add, update, delete)__
* __Set Priority for ToDos__

### Setup

* clone this repo.
```
    git clone https://github.com/rajmani1995/todos-django.git
```
* install Requirements
```
    pip install -r requirements.txt
```
* rename settings.save.py to settings.py and change configuration
```bash
   # Run this commands to migrate the database
   python manage.py migrate
   # create super user (Admin)
   python manage.py createsuperuser
   # Run website
   python manage.py runserver
```

### Requirements

* [Django](https://github.com/django/django)
* Any Database (Sqlite3 preferred)
* [Materialize CSS](https://materializecss.com)
* [Angular JS](https://angularjs.org/)
* [Jquery](https://github.com/jquery/jquery)
