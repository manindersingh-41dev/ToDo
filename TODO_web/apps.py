from django.apps import AppConfig


class TodoWebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TODO_web'

    def ready(self):
        import TODO_web.signals
