from django.apps import AppConfig


class MagasinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'magasin'
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'magasin'
    
    def ready(self):
        import magasin.signals