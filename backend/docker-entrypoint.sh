#!/bin/bash


echo "Waiting for the database to be ready..."
until nc -z -v -w30 db 5432; do
  echo "Waiting for database connection..."
  sleep 1
done
echo "Database is ready!"


echo "Applying migrations..."
python manage.py makemigrations
python manage.py migrate


echo "Deleting and creating superuser..."
python create_superuser.py

echo "Importing Calendar..."
python manage.py import_calendar



echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
