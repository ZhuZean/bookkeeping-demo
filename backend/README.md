# web

## Project setup
```
Create a new virtual environment for Python 3.8
```

### Install the required libraries
```
pip install -r requirements.txt
```

### Config and Start Django
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic --noinput
$ gunicorn --config=gunicorn_config.py backend.wsgi:application
```
