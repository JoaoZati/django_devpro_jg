heroku run python manage.py makemigrations
release: python manage.py migrate
web: gunicorn pypro.wsgi --log-file -
