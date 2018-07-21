from django.shortcuts import render
from rest_framework import serializers
from Homes.models import House,Amenity,HousePictures,HouseVisit
from django.contrib.auth import get_user_model
# Create your views here.



User = get_user_model()




class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePictures
        fields = '__all__'


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]


class HouseSerializer(serializers.Serializer):
    owner = UserSerializer(read_only=True)
    society_amenity = AmenitySerializer(many=True)
    pictures = serializers.SerializerMethodField()
    class Meta:
        model = House
        fields = ['__all__','pictures']

    def get_pictures(self, obj):
        return PictureSerializer(HousePictures.objects.filter(project=obj), many=True).data

class HouseVisitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    house = HouseSerializer(read_only=True)
    class Meta:
        model = HouseVisit
        fields = '__all__'


