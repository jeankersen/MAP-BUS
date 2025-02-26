#!/bin/sh

echo "🛠️ Applying migrations..."
python manage.py makemigrations
python manage.py migrate --noinput

echo "⚙️ Collecting static files..."
python manage.py collectstatic --noinput

echo "👤 Checking and creating superuser if necessary..."
python create_superuser.py

echo "🚀 Starting Django server..."
exec "$@"
