from django.urls import path
from . import views


urlpatterns = [
    path('artist/', views.ArtistCreatelistView.as_view(), name='artist=create-list'),
    path('artist/<int:pk>/', views.ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail-view'),
]
