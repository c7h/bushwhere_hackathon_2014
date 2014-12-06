from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    url = models.URLField()  # for additional urls (Wikipedia...)

class Player(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

class Visit(models.Model):
    player = models.ForeignKey(Player)
    place = models.ForeignKey(Place)

class Hint(models.Model):
    text = models.TextField()
    place = models.ForeignKey(Place)

