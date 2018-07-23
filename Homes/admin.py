from django.contrib import admin
from Homes.models import *

# Register your models here.


@admin.register(HouseVisit)
class HouseVisitModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'house']
    class Meta:
        model = HouseVisit

@admin.register(Amenity)
class HouseVisitModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','category']
    class Meta:
        model = Amenity


@admin.register(SubAmenity)
class HouseVisitModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    class Meta:
        model = SubAmenity

class HomesMediaInline(admin.TabularInline):
    model = HousePicture
    extra = 0


@admin.register(House)
class HouseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner']

    class Meta:
        model = House

    inlines = [
        HomesMediaInline,
    ]
