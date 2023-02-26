from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=70, unique=True, verbose_name='Название исполнителя')

    class Meta:
        verbose_name = ('Артист')
        verbose_name_plural = ('Артисты')

    def __str__(self):
        return f'{self.name}'
