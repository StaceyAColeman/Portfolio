release: python manage.py migrate
web: gunicorn portfolio.wsgi:application --worker-tmp-dir /dev/shm --bind 0.0.0.0:$PORT
