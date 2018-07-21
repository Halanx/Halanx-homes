from django.contrib.auth.decorators import login_required

from .serializer import HouseSerializer, HouseVisitSerializer
from Homes.models import HouseVisit, House

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getAllHomes(request):
    houses = House.objects.all()
    serializer = HouseSerializer(houses, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def getParticularHome(request, pk):
    house = House.objects.filter(pk=pk)
    serializer = HouseSerializer(house, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def postHouseVisit(request):
    if request.method == 'POST':
        housevisit = HouseVisitSerializer(data=request.data)
        if housevisit.is_valid():
            housevisit.save()
        return Response(housevisit.data)


@login_required
@api_view(['GET', 'POST'])
def getScheduledVisits(request):
    user = request.user

    visits = HouseVisit.objects.filter(user=user, is_visited=False)
    serializer = HouseVisitSerializer(visits, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET', 'POST'])
def getVisiteddVisits(request):
    user = request.user
    visits = HouseVisit.objects.filter(user=user, is_visited=False)
    serializer = HouseVisitSerializer(visits, many=True)
    return Response(serializer.data)
