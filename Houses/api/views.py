from django.db.models import Q
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.generics import (RetrieveAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from utility.time_utils import get_datetime

from Common.models import Customer
from Houses.models import House, HouseVisit
from Houses.api.serializers import (HouseVisitSerializer, HouseDetailSerializer, HouseListSerializer,
                                    HouseVisitListSerializer)


class HouseListView(ListAPIView):
    """
    get:
    List all houses (with filters)
    """
    serializer_class = HouseListSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [BasicAuthentication, TokenAuthentication]

    def get_queryset(self):
        params = self.request.query_params
        latitude = params.get('latitude')
        longitude = params.get('longitude')
        radius = params.get('radius', 5)
        rent_max = params.get('rent_max')
        rent_min = params.get('rent_min')
        available_from = params.get('available_from')
        furnish_type = params.get('furnish_type')
        house_type = params.get('house_type')
        accomodation_types = params.get('accomodation_type')
        accomodation_allowed = params.get('accomodation_allowed')
        flat_bhk_count = params.get('flat_bhk_count')
        shared_room_bed_count = params.get('shared_room_bed_count')

        if latitude and longitude:
            queryset = House.objects.nearby(latitude, longitude, radius)
        else:
            queryset = House.objects.filter(visible=True)

        myquery = Q()

        if rent_max:
            myquery &= Q(rent_lte=rent_max)

        if rent_min:
            myquery &= Q(rent_gte=rent_min)

        if available_from:
            myquery &= Q(available_from__lte=get_datetime(available_from))

        if furnish_type:
            myquery &= Q(furnish_type__in=furnish_type.split(','))

        if house_type:
            myquery &= Q(house_type__in=house_type.split(','))

        if accomodation_types:
            myquery &= Q(available_accomodation_types__in=accomodation_types.split(','))

        if accomodation_allowed:
            myquery &= Q(accomodation_allowed__in=accomodation_allowed.split(','))

        if flat_bhk_count:
            myquery &= Q(spaces__flat__bhk_count__in=flat_bhk_count.split(','))

        if shared_room_bed_count:
            myquery &= Q(spaces__shared_room__bed_count__in=shared_room_bed_count.split(','))

        queryset = queryset.filter(myquery)
        return queryset


class HouseRetrieveView(RetrieveAPIView):
    """
    get:
    Retrieve house detail by id
    """
    serializer_class = HouseDetailSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    queryset = House.objects.filter(visible=True)


class HouseVisitListCreateView(ListCreateAPIView):
    """
    get:
    List house visits of customer
    @query_param visited : (true/false)

    post:
    Create a new house visit of customer
    """
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [BasicAuthentication, TokenAuthentication]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HouseVisitListSerializer
        else:
            return HouseVisitSerializer

    def get_queryset(self):
        customer = get_object_or_404(Customer, user=self.request.user)
        visits = customer.house_visits.filter(cancelled=False)
        visited = self.request.query_params.get('visited')
        if visited in [True, False]:
            return visits.filter(visited=visited)
        else:
            return visits

    def create(self, request, *args, **kwargs):
        customer = get_object_or_404(Customer, user=request.user)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=customer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HouseVisitRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve house visit by id

    patch:
    Update house visit by id

    delete:
    Cancel house visit by id
    """
    serializer_class = HouseVisitListSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [BasicAuthentication, TokenAuthentication]

    def get_object(self):
        customer = get_object_or_404(Customer, user=self.request.user)
        return get_object_or_404(HouseVisit, pk=self.kwargs.get('pk'), customer=customer, cancelled=False)

    def destroy(self, request, *args, **kwargs):
        house_visit = self.get_object()
        house_visit.cancelled = True
        house_visit.save()
        return Response({"detail": "Successfully cancelled the visit."}, status=status.HTTP_200_OK)
