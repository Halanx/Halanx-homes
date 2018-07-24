from django.db import models
from Homes.utils import HouseAccomodationTypeCategories
# Create your models here.


class Booking(models.Model):
    room_type = models.CharField(max_length=50,null=False,blank=False,choices=HouseAccomodationTypeCategories)
    room_id = models.IntegerField(null=False,blank=False)
    amount_submited = models.FloatField(null=False,blank=False)
    coupon_code = models.CharField(max_length=50,null=True,blank=True)
    licence_date = models.DateTimeField(null=False,blank=False)
