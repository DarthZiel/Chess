from django.contrib.auth.views import PasswordResetView
from django.urls import path, reverse_lazy
from .views import ChessPlayersListView, ChessPlayersUpdate, check_username, \
    add_chess_player, search, get_chess_player, edit_city_record, delete_chess_player, index, add_players_to_tournament
from players.controllers.users import LoginView, RegisterView, CustomPasswordResetDone, CustomPasswordResetConfirm, \
    CustomPasswordResetCompleteView, CustomPasswordResetView

urlpatterns = [
    path('', index, name='index'),
    path('chess_players/', ChessPlayersListView.as_view(), name='database'),
    path('update_user/<int:pk>/', edit_city_record, name='update_player'),
    path('add_to_tournament', add_players_to_tournament, name='add_players_to_tournament')

]

user_urlpattern = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('password-reset/', CustomPasswordResetView.as_view(),
         name='password_reset_page'),
    path('password-reset/done/', CustomPasswordResetDone.as_view(),
         name='password_reset_done_page'),
    path('password-reset/<uidb64>/<token>/',
         CustomPasswordResetConfirm.as_view(),
         name='password_reset_confirm_page'),
    path('password-reset/complete/',
         CustomPasswordResetCompleteView.as_view(),
         name='password_reset_complete_page'),
]



htmx_urlpatterns = [
    path("check_username/", check_username, name='check_username'),
    path('search/', search, name='search'),
    path("add_player/", add_chess_player, name='add_player'),
    path('get_player/<int:pk>', get_chess_player, name='get_player'),
    path('delete/<int:pk>/', delete_chess_player, name='delete_player'),

]
urlpatterns += user_urlpattern
urlpatterns += htmx_urlpatterns
