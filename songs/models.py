from django.db import models
from genres.models import Genre
from artist.models import Artist


class Song(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='songs')
    release_date = models.DateField(null=True, blank=True)
    artist = models.ManyToManyField(Artist, related_name='songs')
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
