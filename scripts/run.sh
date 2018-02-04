#!/bin/sh
# Wait for db
sleep 5
# restore
python manage.py loaddata data/dump.json
# migration
python manage.py makemigrations
python manage.py migrate
python manage.py createinitialrevisions # django-reversion
# i18n
python manage.py compilemessages
python manage.py collectstatic --noinput
# runserver
export DJANGO_SETTINGS_MODULE=YangSpace.settings.prod
gunicorn YangSpace.wsgi -b 0.0.0.0:8000 --noreload
