from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from app.permissions import GlobalDefaultPermission
from songs.models import Song
from songs.serializers import SongModelSerializer, SongStatsSerializer, SongListDetailSerializer
from reviews.models import Review


class SongCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Song.objects.all()
    # serializer_class = MovieModelSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SongListDetailSerializer
        return SongModelSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        if Song.objects.filter(title=title).exists():
            raise ValidationError(f"A músia '{title}' já existe e não pode ser recriado.")
        serializer.save()


class SongRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SongListDetailSerializer
        return SongModelSerializer


class SongStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Song.objects.all()

    def get(self, request):
        total_songs = self.queryset.count()
        songs_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Review.objects.count()
        average_stars = Review.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_songs': total_songs,
            'songs_by_genre': songs_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0
        }
        serializer = SongStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return response.Response(data=serializer.validated_data, status=status.HTTP_200_OK)
