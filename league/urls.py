from django.urls import path
from . import views

app_name = 'league'
urlpatterns = [
    path('', views.index, name='index'),
    path('p/<int:player_id>', views.player, name='player'),
    path('l/<int:league_id>', views.league, name='league'),
    path('g/<int:game_id>', views.game, name='game'),
]