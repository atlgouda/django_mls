from django.db import models

CONFERENCE_CHOICES = (
    ('Eastern', 'EASTERN'),
    ('Western', 'WESTERN'),
    ('Future', 'FUTURE')
)

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)
    capacity = models.IntegerField()
    joined = models.IntegerField()
    conference = models.CharField(max_length=15, choices=CONFERENCE_CHOICES, default='Eastern')

    def __str__(self):
        return self.name
