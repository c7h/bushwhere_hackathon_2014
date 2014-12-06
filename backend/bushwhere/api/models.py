from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()

    # for additional urls (Wikipedia...)
    url = models.URLField()

class Player(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    # import pdb; pdb.set_trace()

class Hint(models.Model):
    text = models.TextField()
    place = models.ForeignKey(Place)

