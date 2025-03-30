from artist.models import Artist
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from app.permissions import GlobalDefaultPermission
from artist.serializers import ArtistSerializer


class ArtistCreatelistView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    # def create(self, request, *args, **kwargs):
    #     # Verifica se o gênero já existe
    #     artist_name = request.data.get('name')
    #     if Artist.objects.filter(name=artist_name).exists():
    #         raise ValidationError(f'O gênero "{artist_name}" já existe.')
    #     return super().create(request, *args, **kwargs)


class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
