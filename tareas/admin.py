from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from tareas.tasks import send_emails_users
class UserAdmin(UserAdmin):
    actions = ['send_emails_action', 'send_emails_action_False',]

    def send_emails_action(self, request, queryset):
        send_emails_users()
        filas_actualizadas = queryset.update(is_staff = True)

        return True
    
    def send_emails_action_False(self, request, queryset):
        send_emails_users.delay()
        filas_actualizadas = queryset.update(is_staff = False)

        return False

admin.site.unregister(User)     # se "desregistra" User para volver a registrarlo en la siguiente linea
admin.site.register(User, UserAdmin)
