from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import (RetrieveAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,
                                     get_object_or_404)

