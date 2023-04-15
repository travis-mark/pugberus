from django.db import models

class Player(models.Model):
    """A game player"""
    handle = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.handle

class League(models.Model):
    """A league"""
    name = models.CharField(max_length=200)
    players = models.ManyToManyField(Player)
    def __str__(self) -> str:
        return self.name
    
class Game(models.Model):
    """An individual game or match"""
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    game_no = models.IntegerField()
    game_date = models.DateTimeField() # DateField
    result = models.CharField(max_length=200)
    def __str__(self) -> str:
        return f"{self.league.name} #{self.game_no} {self.game_date}" # Date format

class Score(models.Model):
    """One player's performance within a match"""
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()
    guesses = models.CharField(max_length=200) # Optional
    raw_score = models.CharField(max_length=200) # Optional
    def __str__(self) -> str:
        return f'{self.player} {self.game} Score: {self.score}'