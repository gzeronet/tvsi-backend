#!/bin/sh

echo "start db migration"

python manage.py migrate

echo "start load init data, past seven days"

python manage.py load_data --past-seven-days

echo "run web server, visit http://localhost:8000"

python manage.py runserver
