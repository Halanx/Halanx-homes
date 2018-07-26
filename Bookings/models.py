from django.db import models


class Booking(models.Model):
    space = models.ForeignKey('Houses.Space', null=True, on_delete=models.SET_NULL, related_name="bookings")
    rent = models.FloatField()
    deposit = models.FloatField()
    coupon_code = models.CharField(max_length=50, null=True, blank=True)
    licence_date = models.DateTimeField(null=False, blank=False)
