from django.db import models

# Create your models here.


class Place(models.Model):
	name = models.CharField(max_length=100)
	lat = models.FloatField()
	lon = models.FloatField()

	# for additional urls (Wikipedia...)
	url = models.URLField()

class User(models.Model):
	name = models.CharField(max_length=100)

class Hint(models.Model):
	text = models.TextField()
	place = models.ForeignKey(Place)
	
