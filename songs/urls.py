from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.SongCreateListView.as_view(),
         name='song-create-list'),
    path('songs/<int:pk>/', views.SongRetrieveUpdateDestroyView.as_view(),
         name='song-detail-view'),
    path('songs/stats/', views.SongStatsView.as_view(),
         name='song-stats-view'),
]
