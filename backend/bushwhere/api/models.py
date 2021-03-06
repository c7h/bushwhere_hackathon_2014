from django.db import models
import logging

logger = logging.getLogger('api.information')

class Mission(models.Model):
    '''a Mission is a collection of Places in a strict order'''
    name = models.CharField(max_length=100)

    # describe your mission here:
    description = models.TextField()

    # the list of the Places!
    places = models.ManyToManyField('Place', db_table='mission_place_partof')

    def __str__(self):
        return "<Mission %s>" % self.name

class Place(models.Model):
    '''a unique place - can be part of many missions'''
    name = models.CharField(max_length=100)

    # coordinates:
    lat = models.FloatField()
    lon = models.FloatField()

    # for additional urls (Wikipedia...)
    url = models.URLField()

    def __str__(self):
        return '<Place %s>' % self.name

class Player(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #@TODO: player plays missions (many-to-many)

    def __str__(self):
        return "<Player %i>" % self.id

class Visit(models.Model):
    #@TODO: auto-added Timestamp
    player = models.ForeignKey(Player)
    place = models.ForeignKey(Place)

    def save(self, *args, **kwargs):
        super(Visit, self).save(*args, **kwargs)
        logger.info('Player %s visited Place %s' % (self.player.name, self.place.name))

    def __str__(self):
        return "<Visit %i>" % self.id

class Hint(models.Model):
    text = models.TextField()
    place = models.ForeignKey(Place)

    def __str__(self):
        return "<Hint %05i for %s>" % (self.id, self.place.name)

