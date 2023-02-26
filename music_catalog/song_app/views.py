from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from song_app.models import Song
from artist_app.models import Artist

class SongSerializer(ModelSerializer):
    artist_id = PrimaryKeyRelatedField(source='artist', queryset=Artist.objects.all(), required=True)
    artist_name = CharField(source='artist.name', read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'artist_id', 'artist_name']

class SongView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['artist_id']