from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from songs.models import Song


class Review(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(validators=[
        MinValueValidator(0, 'Avaliação não pode ser inferior que 0 estrelas.'),
        MaxValueValidator(5, 'Avaliação não pode ser superior que 5 estrelas.'),
    ]
    )
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.song)
