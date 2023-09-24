#!/bin/bash

cd file_project

python manage.py migrate

gunicorn --bind 0.0.0.0:9000 file_project.wsgi
