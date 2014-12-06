from models import Place, Player, Hint
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
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