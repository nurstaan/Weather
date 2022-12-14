from django.db import models
class City(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 30, verbose_name = 'Имя города')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Города'
        verbose_name_plural = 'Поселки'
