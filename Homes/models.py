from django.db import models
from django.conf import settings
# Create your models here.


HouseTypeCategories = (
    ('Apartment', 'Apartment'),
    ('Independnet', 'Independnet'),
    ('Villa', 'Villa'),
)

FurnishTypeCategories = (
    ('Fully furnished', 'Fully furnished'),
    ('Semi furnished', 'Semi furnished'),
    ('Unfurnished', 'Unfurnished')
)

AccomodationAllowed = (
    ('Girls', 'Girls'),
    ('Boys', 'Boys'),
    ('Family', 'Family')
)

AccomodationType = (
    ('Shared room', 'Shared room'),
    ('Private room', 'Private room'),
    ('Entire house', 'Entire house')
)

AmenityType = (
    ('Inhouse', 'Inhouse'),
    ('Society', 'Society')
)

def get_picture_upload_path(instance, filename):
    return "House/{}/{}/".format(instance.house.id,instance.id)

def get_amenity_picture_upload_path(instance, filename):
    return "Amenity/{}/".format(instance.id)



class SubAmenity(models.Model):
    name = models.CharField(max_length=50)
    pic = models.ImageField(upload_to=get_amenity_picture_upload_path,null=True,blank=True)
    def __str__(self):
        return self.name

class Amenity(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=25, blank=True, null=True, choices=AmenityType)
    sub_amenity = models.ManyToManyField(SubAmenity,related_name='house_sub_amenity')

    def __str__(self):
        return self.name


class House(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    type = models.CharField(max_length=25, blank=True, null=True, choices=HouseTypeCategories)
    rent = models.CharField(max_length=10,blank=True,null=True)
    deposit = models.CharField(max_length=10,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    latitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    furnish_type = models.CharField(max_length=25, blank=True, null=True, choices=FurnishTypeCategories)
    accomodation_allowed = models.CharField(max_length=25, blank=True, null=True, choices=AccomodationAllowed)
    accomodation_type =  models.CharField(max_length=25, blank=True, null=True, choices=AccomodationType)
    accoomodation_count = models.IntegerField(null=True,blank=True)
    available_count = models.IntegerField(null=True,blank=True)
    available_from = models.DateField(null=True,blank=True)
    is_available = models.BooleanField(default=True)
    rules = models.CharField(max_length=500,null=True,blank=True)
    amenity = models.ManyToManyField(Amenity,related_name='house_amenities')

    def __str__(self):
        return self.owner.name

class HousePictures(models.Model):
    house = models.ForeignKey(House,on_delete=models.DO_NOTHING)
    img = models.ImageField(upload_to=get_picture_upload_path, null=True, blank=True)


class HouseVisits(models.Model):
    house = models.ForeignKey(House,on_delete=models.DO_NOTHING,related_name='visit_house')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='user_set')
    date = models.DateTimeField()
    code = models.CharField(max_length=10)
    is_visited = models.BooleanField(default=False)
    



