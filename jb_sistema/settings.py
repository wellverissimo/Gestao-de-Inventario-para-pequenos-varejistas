import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURANÇA: Em produção, use variáveis de ambiente
SECRET_KEY = 'django-insecure-sua-chave-aqui'
DEBUG = True
ALLOWED_HOSTS = []

# Definição dos Apps: Adicione o seu app 'inventario' aqui
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventario', 
]

# Configuração do Banco de Dados conforme seu plano
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'jb_tintas.db', # O arquivo que você já tem
    }
}

# Configurações de Idioma para o Brasil
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
