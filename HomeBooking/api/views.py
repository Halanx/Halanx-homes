from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (RetrieveAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)
from HomeBooking.api.serializers import BookingSerializer
from HomeBooking.models import Booking
from Homes.models import Flat, SharedRoom, PrivateRoom, Customer


class BookingdetailView(RetrieveAPIView):

    def get_object(self):
        room_id =self.kwargs.get('room_id')
        room_type = self.kwargs.get('room_type')
        if room_type=='Flat':
            room = Flat.objects.filter(pk=room_id).first()
            if room:
                return JsonResponse({'rent':room.rent,'desposit':room.deposit})
            else:
                return JsonResponse([],status=status.HTTP_404_NOT_FOUND)
        elif room_type == 'shared_room':
            room = Flat.objects.filter(pk=room_id).first()
            if room:
                return JsonResponse({'rent': room.rent, 'desposit': room.deposit})
            else:
                return JsonResponse([],status=status.HTTP_404_NOT_FOUND)
        elif room_type == 'private_room':
            room = Flat.objects.filter(pk=room_id).first()
            if room:
                return JsonResponse({'rent': room.rent, 'desposit': room.deposit})
            else:
                return JsonResponse([],status=status.HTTP_404_NOT_FOUND)


class BookingListCreateView(ListCreateAPIView):

    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [BasicAuthentication, TokenAuthentication]

    # def create(self, request, *args, **kwargs):
