import os
import django
from dotenv import load_dotenv


load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'map_bus.settings')


django.setup()

from django.contrib.auth import get_user_model


User = get_user_model()

print("Starting create_superuser.py script")


username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if username and email and password:
    print(f"Loaded environment variables:")
    print(f"Username: dans app {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")
else:
    print("Error: Missing required environment variables.")


if username and email and password:
    if not User.objects.filter(username=username).exists():
        try:
            User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser {username} created!")
        except Exception as e:
            print(f"Error creating superuser: {e}")
    else:
        print(f"Superuser {username} already exists.")

