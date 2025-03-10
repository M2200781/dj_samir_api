from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('genres.urls')),

    path('api/v1/', include('artist.urls')),

    path('api/v1/', include('songs.urls')),

    path('api/v1/', include('reviews.urls')),

    path('api/v1/', include('authentication.urls')),
]
