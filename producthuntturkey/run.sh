#!/bin/bash
#pipenv shell

case $1 in
  dev)
    python manage.py runserver --settings=producthuntturkey.settings.local
    ;;
  prod)
    python manage.py makemigrations    
    python manage.py migrate
    python manage.py collectstatic --noinput
    python manage.py runserver --settings=producthuntturkey.settings.prod
    ;;
esac