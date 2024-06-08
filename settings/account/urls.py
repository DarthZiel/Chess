from django.urls import path, re_path
from .views import TournamentListView, add_tournament, TournamentUpdateView, TournamentDeleteView, \
    update_tournament_players, get_tournament_players, remove_player_from_tournament, download_players_excel

app_name = 'account'

urlpatterns = [
    path('', TournamentListView.as_view(), name='tournaments'),
    path('create/', add_tournament, name='add_tournament'),
    path('<int:pk>/update/', TournamentUpdateView.as_view(), name='update_tournament'),
    path('<pk>/delete/', TournamentDeleteView.as_view(), name='delete_tournament'),
    path('update/', update_tournament_players, name='update_tournament_players'),
    path('get/', get_tournament_players, name='get_tournament_players'),
    path('delete/<int:tournament_id>/<int:player_id>/', remove_player_from_tournament,
         name='remove_player_from_tournament'),
    path('download_players/<int:tournament_id>/', download_players_excel, name='download_players_excel')

]
