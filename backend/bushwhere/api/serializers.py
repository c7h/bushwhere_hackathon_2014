from models import Place, Player, Hint, Visit, Mission
from rest_framework import serializers


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('name', 'image')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('name', 'lat', 'lon', 'url')


class HintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hint
        fields = ('text', 'place')

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('player', 'place')

class MissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Mission
       fields = ('id', 'name', 'description', 'places')
            