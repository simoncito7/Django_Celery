from celery import Celery, shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django_celery import settings
import os

# celery = Celery('tasks', broker='amqp://guest@localhost//') #!

# import os

os.environ[ 'DJANGO_SETTINGS_MODULE' ] = "django_celery.settings"
app = Celery('django_celery')

#cuando se agrega un decorador, esto se convierte en una tarea
@shared_task
def send_emails_users():
    asunto = 'Mensaje de prueba'
    mensaje = 'Mensaje de Simón: Hay que ver si me anda Celery con RabbitMQ y Django'
    users = User.objects.all()
    # user_get = User.objects.get(username = 'zorro')
    for user in users:
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [user.email],fail_silently=False)
    return asunto