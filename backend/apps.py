INSTALLED_APPS = [
    #DJANGO APPS DEFAULT
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #THIRD PARTY
    'corsheaders',
    'rest_framework',
    'drf_yasg',
    'dotenv',
    
    #LOCAL APPS
    'apps.example',
    'apps.categoria',
    'apps.recetas'
]