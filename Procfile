web: gunicorn app.wsgi
release: python manage.py makemigrations; python manage.py migrate; python manage.py loaddata --data;
