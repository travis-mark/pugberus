from django.contrib import admin
from .models import Game, League, Player, Score

class ScoreInline(admin.TabularInline):
    model = Score
    extra = 0

class GameAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]
    list_display = ('league_name', 'game_no', 'game_date')
    list_filter = ['game_date']
    def league_name(self, obj):
        return obj.league.name

admin.site.register(League)
admin.site.register(Player)
admin.site.register(Game, GameAdmin)
admin.site.register(Score)
