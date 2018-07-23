from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (RetrieveAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)

from Homes.api.serializers import (HouseVisitSerializer, HouseDetailSerializer, HouseListSerializer,
                                   HouseVisitListSerializer)
from Homes.models import House, Customer, HouseVisit


class HouseListView(ListAPIView):
    """
    get:
    List all houses
    """
    serializer_class = HouseListSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    queryset = House.objects.filter(visible=True)


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
