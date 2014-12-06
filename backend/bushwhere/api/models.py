from django.db import models

# Create your models here.


class Places(models.Model):
	name = models.CharField(max_length=100)
	lat = models.FloatField()
	lon = models.FloatField()

	# for additional urls (Wikipedia...)
	url = models.URLfield()

class User(model.Model):
	name = models.CharField(max_length=100)

class Hint(models.Model):
	text = models.TextField()
	place = models.ForeignKey(Places)
		