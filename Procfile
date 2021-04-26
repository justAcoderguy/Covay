web: python manage.py collectstatic --noinput
web: python manage.py makemigration
web: python manage.py migrate
web: gunicorn mysite.wsgi 