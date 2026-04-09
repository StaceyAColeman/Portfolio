release: python manage.py migrate
web: gunicorn portfolio.wsgi:application --bind 0.0.0.0:8080