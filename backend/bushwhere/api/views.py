from models import Player, Place, Hint, Visit, Mission
from rest_framework import viewsets, status
from serializers import PlayerSerializer, PlaceSerializer, HintSerializer, VisitSerializer, MissionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import path_finder

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows places to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class HintViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hints to be viewed or edited.
    """
    queryset = Hint.objects.all()
    serializer_class = HintSerializer

class VisitViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows visits to be viewed or edited.
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

class MissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows missions to be viewed or edited.
    """
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

@api_view(['GET'])
def next_place(request):
    """
    Get the next place for a player to visit
    """
    player = request.GET.get('player')
    visited_places = Visit.objects.filter(player_id=long(player))
    current_lat = float(request.GET.get('lat'))
    current_lon = float(request.GET.get('lon'))
    data = path_finder.get_next_place((current_lat, current_lon), [(v.place.lat, v.place.lon) for v in visited_places])
    if data:
        serializer = PlaceSerializer(data)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def visit(request):
    """
    Get the next place for a player to visit
    """
    player = request.POST.get('player')
    place = request.POST.get('place')
    Visit(player_id=long(player), place_id=long(place)).save()
    return Response(status=status.HTTP_200_OK)
