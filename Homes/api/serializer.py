from django.shortcuts import render
from rest_framework import serializers
from Homes.models import *
from django.contrib.auth import get_user_model
# Create your views here.



User = get_user_model()


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePicture
        fields = '__all__'


class HouseOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseOwner
        fields = '__all__'

class HouseSerializer(serializers.Serializer):
    owner = HouseOwnerSerializer(read_only=True)
    shared_rooms = serializers.SerializerMethodField()
    private_rooms = serializers.SerializerMethodField()
    flats = serializers.SerializerMethodField()
    pictures = serializers.SerializerMethodField()
    amenity = serializers.SerializerMethodField()
    monthly_expense = serializers.SerializerMethodField()
    class Meta:
        model = House
        fields = ['__all__','pictures']

    def get_pictures(self, obj):
        return PictureSerializer(HousePicture.objects.filter(house=obj), many=True).data

    def get_shared_rooms(self, obj):
        return SharedRoomSerializer(SharedRoom.objects.filter(house=obj), many=True).data

    def get_private_rooms(self, obj):
        return PrivateRoomSerializer(PrivateRoom.objects.filter(house=obj), many=True).data

    def get_flats(self, obj):
        return Flat(Flat.objects.filter(house=obj), many=True).data

    def get_amenity(self, obj):
        return HouseSerializer(HouseAmenity.objects.filter(house=obj), many=True).data

    def get_monthly_expense(self, obj):
        return MonthlyExpenseSerializer(HouseMonthlyExpense.objects.filter(house=obj), many=True).data



class HouseListSerializer1(serializers.Serializer):
    pictures = serializers.SerializerMethodField()
    class Meta:
        model = House
        fields = ['name','street_address','pictures']

    def get_pictures(self, obj):
        return PictureSerializer(HousePicture.objects.filter(house=obj), many=True).data


class PrivateRoomSerializer(serializers.Serializer):
    house = HouseSerializer(read_only=True)
    class Meta:
        models = PrivateRoom
        fields='__all__'


class SharedRoomSerializer(serializers.Serializer):
    house = HouseSerializer(read_only=True)
    shared_bed = serializers.SerializerMethodField()
    class Meta:
        models = SharedRoom
        fields=['__all__','shared_bed']

    def get_shared_bed(self,obj):
        return PictureSerializer(Bed.objects.filter(room=obj), many=True).data

class FlatRoomSerializer(serializers.Serializer):
    house = HouseSerializer(read_only=True)
    class Meta:
        models = Flat
        fields='__all__'

class MonthlyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseMonthlyExpense
        fields = '__all__'

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class HouseAmenitySerializer(serializers.ModelSerializer):
    amenity = AmenitySerializer(many=True)
    class Meta:
        model = HouseAmenity
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

class HouseVisitSerializer(serializers.ModelSerializer):
    customer = UserSerializer(read_only=True)
    house = HouseSerializer(read_only=True)
    class Meta:
        model = HouseVisit
        fields = '__all__'


