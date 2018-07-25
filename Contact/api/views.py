from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Contact.models import *

from Contact.api.serializers import (
  FormSubmitionSerializer
)


@api_view(['POST'])
def ContactformSubmittion(request):
    if request.method=='POST':

        submit = FormSubmitionSerializer(data=request.data)
        if submit.is_valid():
            submit.save()
        return Response(submit.data,status=status.HTTP_201_CREATED)


