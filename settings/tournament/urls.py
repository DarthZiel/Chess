from .views import TournamentList, search, TournamentDetailView
from django.urls import path

app_name = 'tournament'
urlpatterns = [
    path('', TournamentList.as_view(), name='tournaments'),
    path('search/', search, name='search'),
    path('detail/<int:pk>', TournamentDetailView.as_view(), name='detail_tournament')
]
