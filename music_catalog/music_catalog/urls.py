"""music_catalog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from artist_app.views import ArtistView
from song_app.views import SongView
from album_app.views import AlbumView, AlbumSongView

router = SimpleRouter()

router.register('api/artists', ArtistView)
router.register('api/songs', SongView)
router.register('api/albums', AlbumView)
router.register('api/albumsong', AlbumSongView)

schema_view = get_schema_view(
   openapi.Info(
        default_version = "v1",
        title = "Music Catalog API",
        description = "Тестовое задание для Кортекс",
        contact = openapi.Contact(email="buchkonikita97@gmail.com"),
   ),
   public = True,
   permission_classes = (permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls)]

urlpatterns += router.urls

urlpatterns += [re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')]