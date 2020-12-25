from django.shortcuts import render
import string
from django.contrib.auth.models import User # User es la tabla que se genera por defecto en el sistema
from django.utils.crypto import get_random_string


def create_user_randomly(cantidad):
    for i in range(cantidad):
        username = 'usuario_{}'.format(get_random_string(5, string.ascii_letters))
        email = '{}@dominio.ar'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return('{} usuarios creados correctamente').format(i)