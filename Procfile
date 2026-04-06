release: python manage.py migrate
web: gunicorn --worker-tmp-dir /dev/shm portfolio.wsgi
