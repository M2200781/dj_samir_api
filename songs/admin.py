from django.contrib import admin
from songs.models import Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'resume')
