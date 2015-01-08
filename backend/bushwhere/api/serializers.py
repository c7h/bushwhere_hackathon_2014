from models import Place, Player, Hint, Visit, Mission
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields =  ('username', 'first_name', 'last_name' ,'email', 'image')

    def get_image(self, obj):
        return obj.player.image


class PlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=False)

    class Meta:
        model = Player
        fields = ('id', 'user', 'image')


class HintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hint
        fields = ('id', 'text')


class PlaceSerializer(serializers.ModelSerializer):
    hints = HintSerializer(read_only=False, many=True)

    class Meta:
        model = Place
        fields = ('id', 'name', 'lat', 'lon', 'url', 'hints')


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visit
        fields = ('player', 'place')

class MissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Mission
       fields = ('id', 'name', 'description', 'places')

