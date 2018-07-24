from random import randint

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.safestring import mark_safe

from multiselectfield import MultiSelectField

from Homes.utils import (HouseTypeCategories, HouseFurnishTypeCategories, HouseAccomodationAllowedCategories,
                         HouseAccomodationTypeCategories, AmenityTypeCategories, get_house_picture_upload_path,
                         get_amenity_picture_upload_path, get_sub_amenity_picture_upload_path, FLAT,
                         get_house_owner_profile_pic_upload_path, default_profile_pic_url, SHARED_ROOM, PRIVATE_ROOM)


class MonthlyExpenseCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Monthly expense categories`'

    def __str__(self):
        return self.name


class HouseMonthlyExpense(models.Model):
    house = models.ForeignKey('House', on_delete=models.CASCADE, related_name='monthly_expenses')
    category = models.ForeignKey('MonthlyExpenseCategory', on_delete=models.CASCADE,
                                 related_name='house_monthly_expenses')
    accomodation_type = models.CharField(max_length=25, choices=HouseAccomodationTypeCategories, default=FLAT)
    amount = models.FloatField()

    def __str__(self):
        return str(self.id)


class Amenity(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=25, blank=True, null=True, choices=AmenityTypeCategories)
    image = models.ImageField(upload_to=get_amenity_picture_upload_path, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Amenities'

    def __str__(self):
        return self.name

    def get_amenity_image_html(self):
        if self.image:
            return mark_safe('<img src="{}" width="80" height="80" />'.format(self.image.url))
        else:
            return None

    get_amenity_image_html.short_description = 'Amenity Image'
    get_amenity_image_html.allow_tags = True


class SubAmenity(models.Model):
    name = models.CharField(max_length=50)
    amenity = models.ForeignKey('Amenity', on_delete=models.CASCADE, related_name='sub_amenities')
    image = models.ImageField(upload_to=get_sub_amenity_picture_upload_path, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Sub Amenities'

    def __str__(self):
        return self.name

    def get_sub_amenity_image_html(self):
        if self.image:
            return mark_safe('<img src="{}" width="80" height="80" />'.format(self.image.url))
        else:
            return None

    get_sub_amenity_image_html.short_description = 'SubAmenity Image'
    get_sub_amenity_image_html.allow_tags = True


class HouseAmenity(models.Model):
    house = models.ForeignKey('House', on_delete=models.CASCADE, related_name='amenities')
    amenity = models.ForeignKey('Amenity', on_delete=models.CASCADE, related_name='house_amenities')
    sub_amenities = models.ManyToManyField('SubAmenity', related_name='house_sub_amenities')
    count = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = 'House Amenities'

    def __str__(self):
        return str(self.id)


class Bed(models.Model):
    room = models.ForeignKey('SharedRoom', on_delete=models.PROTECT, related_name='beds')
    bed_no = models.CharField(max_length=10, blank=True, null=True)

    available = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class SharedRoom(models.Model):
    space = models.OneToOneField('Space', on_delete=models.PROTECT, null=True, related_name='shared_room')
    sharing_limit = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def available(self):
        return self.space.available

    @property
    def bed_count(self):
        return self.beds.filter(visible=True).count()

    @property
    def free_bed_count(self):
        return self.beds.filter(available=True, visible=True).count()


class PrivateRoom(models.Model):
    space = models.OneToOneField('Space', on_delete=models.PROTECT, null=True, related_name='private_room')

    def __str__(self):
        return str(self.id)

    @property
    def available(self):
        return self.space.available


class Flat(models.Model):
    space = models.OneToOneField('Space', on_delete=models.PROTECT, null=True, related_name='flat')
    bhk_count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def available(self):
        return self.space.available


class Space(models.Model):
    house = models.ForeignKey('House', on_delete=models.PROTECT, related_name='spaces')
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=20, choices=HouseAccomodationTypeCategories)

    rent = models.FloatField()
    deposit = models.FloatField()

    available = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)


class House(models.Model):
    owner = models.ForeignKey('HouseOwner', on_delete=models.PROTECT, related_name='houses')
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rules = models.TextField(null=True, blank=True)
    cover_pic_url = models.CharField(max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    available_from = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)
    visible = models.BooleanField(default=True)

    street_address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    house_type = models.CharField(max_length=25, blank=True, null=True, choices=HouseTypeCategories)
    furnish_type = models.CharField(max_length=25, blank=True, null=True, choices=HouseFurnishTypeCategories)
    available_accomodation_types = MultiSelectField(max_length=25, max_choices=3,
                                                    choices=HouseAccomodationTypeCategories)
    accomodation_allowed = MultiSelectField(max_length=25, max_choices=3, choices=HouseAccomodationAllowedCategories)

    def __str__(self):
        return str(self.name)

    def get_monthly_expenses(self, accomodation_type=FLAT):
        return self.monthly_expenses.filter(accomodation_type=accomodation_type)

    @property
    def flats(self):
        return Flat.objects.filter(space__house=self)

    @property
    def private_rooms(self):
        return PrivateRoom.objects.filter(space__house=self)

    @property
    def shared_rooms(self):
        return SharedRoom.objects.filter(space__house=self)


class HouseOwner(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(upload_to=get_house_owner_profile_pic_upload_path, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def name(self):
        return self.user.get_full_name()


class HousePicture(models.Model):
    house = models.ForeignKey(House, on_delete=models.DO_NOTHING, related_name='pictures')
    image = models.ImageField(upload_to=get_house_picture_upload_path, null=True, blank=True)
    is_cover_pic = models.BooleanField(default=False)
    rank = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if self.is_cover_pic:
            self.house.cover_pic_url = self.image.url
            self.house.save()
            last_cover_pic = self.house.pictures.filter(is_cover_pic=True).first()
            if last_cover_pic:
                last_cover_pic.is_cover_pic = False
                last_cover_pic.save()

        super(HousePicture, self).save(*args, **kwargs)


class HouseVisit(models.Model):
    house = models.ForeignKey('House', on_delete=models.SET_NULL, null=True, related_name='visits')
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, related_name='house_visits')
    code = models.CharField(max_length=10, blank=True, null=True)
    scheduled_visit_time = models.DateTimeField()

    visited = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    actual_visit_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            self.code = str(randint(111111, 999999))
        super(HouseVisit, self).save(*args, **kwargs)


class Customer(models.Model):
    """
    This class will be later replaced by Halanx customer class
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200, null=True)
    profile_pic_url = models.CharField(max_length=500, blank=True, null=True, default=default_profile_pic_url)

    def __str__(self):
        return str(self.id)

    @property
    def name(self):
        return self.user.get_full_name()


# noinspection PyUnusedLocal
@receiver(post_save, sender=Space)
def update_house_availability(sender, instance, **kwargs):
    house = instance.house
    house.available = True if house.spaces.filter(visible=True, available=True).count() else False
    house.save()


# noinspection PyUnusedLocal
@receiver(post_save, sender=Bed)
def update_room_availability(sender, instance, **kwargs):
    room = instance.room
    room.space.available = True if room.beds.filter(visible=True, available=True).count() else False
    room.space.save()


# noinspection PyUnusedLocal
@receiver(post_save, sender=Space)
def create_space_type_object(sender, instance, created, **kwargs):
    if instance.type == FLAT:
        Flat.objects.get_or_create(space=instance)
        SharedRoom.objects.filter(space=instance).delete()
        PrivateRoom.objects.filter(space=instance).delete()
    elif instance.type == SHARED_ROOM:
        SharedRoom.objects.get_or_create(space=instance)
        Flat.objects.filter(space=instance).delete()
        PrivateRoom.objects.filter(space=instance).delete()
    elif instance.type == PRIVATE_ROOM:
        PrivateRoom.objects.get_or_create(space=instance)
        SharedRoom.objects.filter(space=instance).delete()
        Flat.objects.filter(space=instance).delete()
