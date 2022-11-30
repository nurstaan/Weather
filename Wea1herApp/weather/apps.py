from django.apps import AppConfig

class WeatherConfig(AppConfig):
    name = 'weather'
    verbose_name = 'Прогноз погоды'
    default_auto_field = 'django.db.models.AutoField'
