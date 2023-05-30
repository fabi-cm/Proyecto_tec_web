from django.apps import AppConfig


class ApiMusicaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_musica'

    def ready(self):
        import api_musica.signals
