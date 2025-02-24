import os
import django
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Assure-toi que cette ligne est présente dans ton script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'map_bus.settings')

# Initialiser Django
django.setup()

from django.contrib.auth import get_user_model

# Récupérer le modèle utilisateur personnalisé
User = get_user_model()

print("Starting create_superuser.py script")

# Récupérer les données depuis les variables d'environnement
username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

# Vérifier si les variables sont bien chargées
if username and email and password:
    print(f"Loaded environment variables:")
    print(f"Username: dans app {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")
else:
    print("Error: Missing required environment variables.")

# Créer le superutilisateur si nécessaire
if username and email and password:
    if not User.objects.filter(username=username).exists():
        try:
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser {username} created!")
        except Exception as e:
            print(f"Error creating superuser: {e}")
    else:
        print(f"Superuser {username} already exists.")

# Créer d'autres utilisateurs
for i in range(1, 4):
    username = os.getenv(f'DJANGO_USER_{i}_USERNAME')
    email = os.getenv(f'DJANGO_USER_{i}_EMAIL')
    password = os.getenv(f'DJANGO_USER_{i}_PASSWORD')

    if username and email and password:
        print(f"Creating user {i}: {username}")
        try:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, email=email, password=password)
                print(f"User {username} created!")
            else:
                print(f"User {username} already exists.")
        except Exception as e:
            print(f"Error creating user {username}: {e}")
    else:
        print(f"Error: Missing data for user {i}.")
