from django.contrib import admin
from Houses.models import (House, HousePicture, HouseMonthlyExpense, HouseAmenity, Amenity, SubAmenity,
                           HouseVisit, MonthlyExpenseCategory, Space, Flat, PrivateRoom, SharedRoom)
from Houses.utils import FLAT, PRIVATE_ROOM, SHARED_ROOM


@admin.register(HouseVisit)
class HouseVisitModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'house', 'customer', 'scheduled_visit_time', 'visited')

    class Meta:
        model = HouseVisit


@admin.register(Amenity)
class AmenityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'get_amenity_image_html')
    readonly_fields = ('get_amenity_image_html',)

    class Meta:
        model = Amenity


@admin.register(SubAmenity)
class SubAmenityModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_sub_amenity_image_html')
    readonly_fields = ('get_sub_amenity_image_html',)

    class Meta:
        model = SubAmenity


@admin.register(MonthlyExpenseCategory)
class MonthlyExpenseCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    class Meta:
        model = MonthlyExpenseCategory


class HousePictureInline(admin.TabularInline):
    model = HousePicture
    extra = 0


class HouseInline(admin.TabularInline):
    model = House
    extra = 0


class HouseAmenityInline(admin.TabularInline):
    model = HouseAmenity
    extra = 1


class HouseMonthlyExpenseInline(admin.TabularInline):
    model = HouseMonthlyExpense
    extra = 1


class FlatInline(admin.TabularInline):
    model = Flat
    extra = 0


class SharedRoomInline(admin.TabularInline):
    model = SharedRoom
    extra = 0


class PrivateRoomInline(admin.TabularInline):
    model = PrivateRoom
    extra = 0


@admin.register(House)
class HouseModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'available')

    class Meta:
        model = House

    inlines = (
        HousePictureInline,
        HouseAmenityInline,
        HouseMonthlyExpenseInline,
    )


@admin.register(Space)
class SpaceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'house', 'name', 'available', 'visible')

    class Meta:
        model = Space

    inlines = (
        FlatInline,
        PrivateRoomInline,
        SharedRoomInline
    )

    def get_inline_instances(self, request, obj=None):
        # Return no inlines when obj is being created
        if not obj:
            return []

        inline_instances = super(SpaceModelAdmin, self).get_inline_instances(request, obj)
        if obj.type == FLAT:
            return [x for x in inline_instances if isinstance(x, FlatInline)]
        elif obj.type == PRIVATE_ROOM:
            return [x for x in inline_instances if isinstance(x, PrivateRoomInline)]
        elif obj.type == SHARED_ROOM:
            return [x for x in inline_instances if isinstance(x, SharedRoomInline)]
        else:
            return []


@admin.register(Flat)
class FlatModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'space', 'bhk_count')

    class Meta:
        model = Flat


@admin.register(PrivateRoom)
class PrivateRoomModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'space')

    class Meta:
        model = PrivateRoom


@admin.register(SharedRoom)
class SharedRoomModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'space', 'sharing_limit')

    class Meta:
        model = SharedRoom
