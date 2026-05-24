from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

from django.db.models.signals import post_migrate

def create_superuser(sender, **kwargs):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='carlos',
            email='carlos213244@gmail.com',
            password='jose2306'
        )
        print("Superusuario creado automáticamente")

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        post_migrate.connect(create_superuser, sender=self)
