from genres.models import Genre
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from app.permissions import GlobalPermission
from genres.serializers import GenreSerializer


# Create your views here.
# Cria e Lista

class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def create(self, request, *args, **kwargs):
        # Verifica se o gênero já existe
        genre_name = request.data.get('name')
        if Genre.objects.filter(name=genre_name).exists():
            raise ValidationError(f'O gênero "{genre_name}" já existe.')
        # Chama o método create original se o gênero não existir
        return super().create(request, *args, **kwargs)


# Recupera, Modifica e deleta a partir de uma seleção por id (PUT/DELETE)
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalPermission,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
