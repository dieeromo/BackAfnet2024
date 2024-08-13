from django.apps import AppConfig


class InversionesempresaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inversionesEmpresa'
    def ready(self):
        import inversionesEmpresa.signals
# 