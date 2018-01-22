#!/bin/sh
# Wait for db
sleep 5
# migration
python manage.py makemigrations
python manage.py migrate
# i18n
python manage.py compilemessages
# runserver
python manage.py runserver 0.0.0.0:8000
