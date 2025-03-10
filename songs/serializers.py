from django.db.models import Avg
from rest_framework import serializers
from songs.models import Song
# from genres.models import Genre
from genres.serializers import GenreSerializer
# from actors.models import Actor
from artist.serializers import ArtistSerializer


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(),
#     )
#     release_date = serializers.DateField()
#     actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True,
#     )

class SongModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1980:
            raise serializers.ValidationError('Sómente filmes com lançamentos a patir de 1980.')
        else:
            return value

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O resumo se limita ao máximo de 200 caracteres.')
        else:
            return value


class SongListDetailSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Song
        fields = ['id', 'title', 'genre', 'artist', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)
        return None


class SongStatsSerializer(serializers.Serializer):
    total_songs = serializers.IntegerField()
    songs_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
