#!/usr/bin/env python3
python manage.py migrate
python manage.py runserver 0.0.0.0:8000 --settings=pictureserver_django.local_settings
