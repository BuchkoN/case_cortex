from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from artist_app.models import Artist


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class ArtistView(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
