from django.db import models

class Team(models.Model):
    name  = models.CharField(max_length = 100)
    standings = models.CharField(max_length = 2)
    wins = models.CharField(max_length = 3)
    draws = models.CharField(max_length = 3)
    losses = models.CharField(max_length = 3)

    def __str__(self):
        return self.name
