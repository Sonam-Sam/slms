from django.apps import AppConfig


class AdminSsoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_sso'

    def ready(self):
        import admin_sso.signals
