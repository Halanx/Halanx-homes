from django.contrib import admin
from Homes.models import (House, HousePicture, HouseOwner, HouseMonthlyExpense, HouseAmenity, Amenity, SubAmenity,
                          HouseVisit, MonthlyExpenseCategory)


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


@admin.register(HouseOwner)
class HouseOwnerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

    class Meta:
        model = HouseOwner

    inlines = (
        HouseInline,
    )
