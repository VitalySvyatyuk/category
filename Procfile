web: python manage.py runserver
web: gunicorn category.wsgi --log-file -
heroku ps:scale web=1