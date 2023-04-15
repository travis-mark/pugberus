from django.contrib import admin

from league.models import Game, League, Player, Score

admin.site.register(League)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Score)
