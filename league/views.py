from django.shortcuts import get_object_or_404, render

from league.models import Game, League, Player

def index(request):
    leagues = League.objects.all()
    context = {
        'leagues': leagues,
    }
    return render(request, 'league/index.html', context)

def league(request, league_id):
    _league = get_object_or_404(League, pk=league_id)
    return render(request, 'league/league.html', {'league': _league})

def player(request, player_id):
    _player = get_object_or_404(Player, pk=player_id)
    return render(request, 'league/player.html', {'player': _player})

def game(request, game_id):
    _game = get_object_or_404(Game, pk=game_id)
    return render(request, 'league/game.html', {'game': _game})
