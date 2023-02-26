from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField, PrimaryKeyRelatedField
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from album_app.models import Album, AlbumSong
from artist_app.models import Artist
from song_app.models import Song

class AlbumSerializer(ModelSerializer):
    artist_id = PrimaryKeyRelatedField(source='artist', queryset = Artist.objects.all(), required=True)
    artist_name = CharField(read_only=True, source='artist.name')
    songs = SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'name', 'year_release', 'artist_id', 'artist_name', 'songs']
    
    def get_songs(self, obj):
        objects = AlbumSong.objects.filter(album=obj)
        return [{'song_id': object.song.pk, 'title': object.song.title, 'position': object.position}
                for object in objects]

class AlbumSongSerializer(ModelSerializer):
    album_id = PrimaryKeyRelatedField(source='album', queryset = Album.objects.all(), required=True)
    song_id = PrimaryKeyRelatedField(source='song', queryset = Song.objects.all(), required=True)
    album_name = CharField(read_only=True, source='album.name')
    song_name = CharField(read_only=True, source='song.title')

    class Meta:
        model = AlbumSong
        fields = ['id', 'album_id', 'album_name', 'song_id', 'song_name', 'position']
    
class AlbumView(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['artist_id']

class AlbumSongView(ModelViewSet):
    queryset = AlbumSong.objects.all()
    serializer_class = AlbumSongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['album_id', 'song_id']

    def create(self, request):
        album = Album.objects.get(id=request.data['album_id'])
        song = Song.objects.get(id=request.data['song_id'])
        if album.artist.name == song.artist.name:
            return super().create(request)
        else:
            return Response(status=400, data="fields 'artist' don't match in song and album")