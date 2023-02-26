from django.db import models
from artist_app.models import Artist

class Song(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название песни')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Артист')

    class Meta:
        verbose_name = ('Песня')
        verbose_name_plural = ('Песни')
        unique_together = ('title', 'artist')

    def __str__(self):
        return f'{self.title} ({self.artist.name})'