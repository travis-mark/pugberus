from django.contrib import admin
from .models import Game, League, Player, Score

class ScoreInline(admin.TabularInline):
    model = Score
    extra = 0

class GameAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]
    #list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(League)
admin.site.register(Player)
admin.site.register(Game, GameAdmin)
admin.site.register(Score)
