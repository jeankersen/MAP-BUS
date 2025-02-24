#!/bin/bash

# Attendre que la base de données soit prête
echo "Waiting for the database to be ready..."
until nc -z -v -w30 db 5432; do
  echo "Waiting for database connection..."
  sleep 1
done
echo "Database is ready!"

# Appliquer les migrations
echo "Applying migrations..."
python manage.py migrate

# Supprimer et recréer le superutilisateur
echo "Deleting and creating superuser..."
python create_superuser.py

# Démarrer le serveur Django
echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000
