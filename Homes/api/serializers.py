from rest_framework import serializers
from utility.serializers import DateTimeFieldTZ

from Homes.models import (House, Flat, SharedRoom, PrivateRoom, HousePicture, HouseVisit,
                          HouseAmenity, Amenity, HouseOwner, Customer, Bed, HouseMonthlyExpense, SubAmenity, Space)


class HousePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePicture
        fields = '__all__'


class HouseMonthlyExpenseSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = HouseMonthlyExpense
        fields = '__all__'

    @staticmethod
    def get_category(obj):
        return obj.category.name


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'


class SubAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubAmenity
        fields = '__all__'


class HouseAmenitySerializer(serializers.ModelSerializer):
    amenity = AmenitySerializer()
    sub_amenities = SubAmenitySerializer(many=True)

    class Meta:
        model = HouseAmenity
        fields = '__all__'


class HouseOwnerBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseOwner
        fields = ('name', 'profile_pic')


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        exclude = ('visible',)


class PrivateRoomSerializer(serializers.ModelSerializer):
    space = SpaceSerializer()

    class Meta:
        model = PrivateRoom
        fields = '__all__'


class BedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bed
        exclude = ('visible',)


class SharedRoomSerializer(serializers.ModelSerializer):
    space = SpaceSerializer()
    beds = serializers.SerializerMethodField()
    bed_count = serializers.IntegerField()
    free_bed_count = serializers.IntegerField()

    class Meta:
        model = SharedRoom
        fields = '__all__'

    @staticmethod
    def get_beds(obj):
        return BedSerializer(obj.beds.filter(visible=True), many=True).data


class FlatSerializer(serializers.ModelSerializer):
    space = SpaceSerializer()

    class Meta:
        model = Flat
        fields = '__all__'


class HouseDetailSerializer(serializers.ModelSerializer):
    owner = HouseOwnerBasicSerializer()
    pictures = HousePictureSerializer(many=True)
    monthly_expenses = HouseMonthlyExpenseSerializer(many=True)
    amenities = HouseAmenitySerializer(many=True)

    private_rooms = serializers.SerializerMethodField()
    shared_rooms = serializers.SerializerMethodField()
    flats = serializers.SerializerMethodField()

    class Meta:
        model = House
        exclude = ('created_at', 'modified_at', 'visible')

    @staticmethod
    def get_private_rooms(obj):
        return PrivateRoomSerializer(obj.private_rooms.filter(space__visible=True), many=True).data

    @staticmethod
    def get_shared_rooms(obj):
        return SharedRoomSerializer(obj.shared_rooms.filter(space__visible=True), many=True).data

    @staticmethod
    def get_flats(obj):
        return FlatSerializer(obj.flats.filter(space__visible=True), many=True).data


class HouseListSerializer(serializers.ModelSerializer):
    pictures = HousePictureSerializer(many=True)

    class Meta:
        model = House
        exclude = ('owner', 'created_at', 'modified_at', 'visible')


class HouseBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        exclude = ('owner', 'rules', 'created_at', 'modified_at', 'visible')


class HouseVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseVisit
        fields = '__all__'


class CustomerBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', 'profile_pic_url')


class HouseVisitListSerializer(serializers.ModelSerializer):
    house = HouseBasicSerializer()
    customer = CustomerBasicSerializer()
    scheduled_visit_time = DateTimeFieldTZ()
    actual_visit_time = DateTimeFieldTZ()

    class Meta:
        model = HouseVisit
        fields = '__all__'
