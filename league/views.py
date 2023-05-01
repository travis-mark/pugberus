from django.db.models import Avg, Min, Max, Count, Func, FloatField
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
    _players = _league.game_set.values('score__player__handle', 'score__player__id').annotate(
        avg_score=Func(Avg('score__score'), 1, function='ROUND', output_field=FloatField()),
        min_score=Min('score__score'),
        max_score=Max('score__score'),
        count=Count('id')
    )
    _games = _league.game_set.order_by('-game_no').all()
    return render(request, 'league/league.html', {'league': _league, 'games': _games, 'players': _players})

def player(request, player_id):
    _player = get_object_or_404(Player, pk=player_id)
    _scores = _player.score_set.order_by('game__league__name', '-game__game_no')
    _leagues = _player.score_set.values('game__league__name', 'game__league__id').annotate(
        avg_score=Func(Avg('score'), 1, function='ROUND', output_field=FloatField()),
        min_score=Min('score'),
        max_score=Max('score'),
        count=Count('id')
    )
    return render(request, 'league/player.html', {'player': _player, 'scores': _scores, 'leagues': _leagues})

def game(request, game_id):
    _game = get_object_or_404(Game, pk=game_id)
    return render(request, 'league/game.html', {'game': _game})

def chart(request, league_id):
    _league = get_object_or_404(League, pk=league_id)
    _games = _league.game_set.order_by('-game_no').all()
    return render(request, 'league/chart.html', {'league': _league, 'games': _games})
