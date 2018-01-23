#!/bin/sh
# Wait for db
sleep 5
# migration
python manage.py makemigrations
python manage.py migrate
# i18n
python manage.py compilemessages
python manage.py collectstatic --noinput
# runserver
export DJANGO_SETTINGS_MODULE=YangSpace.settings.prod 
gunicorn YangSpace.wsgi -b 0.0.0.0:8000
