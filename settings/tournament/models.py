from django.db import models
from players.models import User, ChessPlayers, Region
TYPE_CHOICES = [
    ('open', 'Open'),
    ('man', 'Man'),
    ('woman', 'Woman'),
]


# Create your models here.
class Tournament(models.Model):
    title = models.CharField('', max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    gender = models.CharField(max_length=5, choices=TYPE_CHOICES, default='open')
    has_age_limit = models.BooleanField(default=False)
    min_age = models.PositiveIntegerField(blank=True, null=True)
    max_age = models.PositiveIntegerField(blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    players = models.ManyToManyField(ChessPlayers, related_name='tournaments')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title