from models import Place, Player, Hint, Visit, Mission
from rest_framework import serializers


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id','name', 'image')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'lat', 'lon', 'url')


class HintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hint
        fields = ('id', 'text', 'place')

class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ('player', 'place')

class MissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Mission
       fields = ('id', 'name', 'description', 'places')
            