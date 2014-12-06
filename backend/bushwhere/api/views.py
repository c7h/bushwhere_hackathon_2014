# Create your views here.

from models import User, Place, Hint
from rest_framework import viewsets, status
from models import Player, Place, Hint
from serializers import UserSerializer, PlaceSerializer, HintSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import path_finder

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = UserSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class HintViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Hint.objects.all()
    serializer_class = HintSerializer

@api_view(['GET'])
def next_place(request):
    """
    Get the next place for a user to visit
    """
    user = request.GET.get('user')
    current_lat = float(request.GET.get('lat'))
    current_lon = float(request.GET.get('lon'))
    data = path_finder.get_next_place((current_lat, current_lon), [(0.0, 0.0)])
    if data:
        serializer = PlaceSerializer(data)
        return Response(serializer.data)
    return Response(status=status.HTTP_204_NO_CONTENT)
