# Users Tasks csv file

## Technologies
* Python 3.X
* Django 4.0
* requests module
* csv module


## Installation

Clone the github repository to your directory.

```bash
git clone https://github.com/adrianbuskiewicz/Users-Tasks-Project.git
```

Create and activate virtual environment.

```bash
py -m venv venv
venv\Scripts\activate
```

Install needed packages.

```bash
(venv) cd Users-Tasks-Project
(venv) pip install -r requirements.txt
```

Migrate models to the database.

```bash
(venv) py manage.py makemigrations
(venv) py manage.py migrate
```

Create admin (superuser).

```bash
(venv) py manage.py createsuperuser
```

Run server at 8080 port.

```bash
(venv) py manage.py runserver 8080
```

## Usage


To download csv file:
\
localhost:8080/app/user_task

Or click here after running server: [app/user_task](http://localhost:8080/app/user_task)

```bash
(venv) py manage.py test
```


## Testing

To start testing app you need to use:

```bash
(venv) py manage.py test
```
