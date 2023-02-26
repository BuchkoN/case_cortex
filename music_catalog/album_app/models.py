from django.db import models
from artist_app.models import Artist
from song_app.models import Song

class Album(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название альбома')
    year_release = models.PositiveIntegerField(verbose_name='Год выпуска')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name='Исполнитель')
    songs = models.ManyToManyField(Song, through='AlbumSong')

    class Meta:
        verbose_name = ('Альбом')
        verbose_name_plural = ('Альбомы')
        unique_together = ('name', 'artist')

    def __str__(self):
        return f'{self.name} {self.year_release} ({self.artist})'
    
class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='Исполнитель')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='Песня')
    position = models.PositiveIntegerField(verbose_name='Позиция в альбоме')

    class Meta:
        unique_together = ('song', 'position')