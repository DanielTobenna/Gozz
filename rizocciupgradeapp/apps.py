from django.apps import AppConfig


class RizocciupgradeappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rizocciupgradeapp'

    def ready(self):
    	import rizocciupgradeapp.signals
