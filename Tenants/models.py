from datetime import date, timedelta

from dirtyfields import DirtyFieldsMixin
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from geopy import units, distance



DocumentType = (
    ('Id','Id'),
    ('Employment','Employment'),
    ('Other', 'Other'),
)

TransactionType = (
    ('Credit','Credit'),
    ('Debit','Debit')
)

def upload_documents(instance, filename):
    return "tenant/{}/documents/{}-{}".format(instance.tenant.id, instance.tenant.id, filename)


class Customer(models.Model):
    """
    This class will be later replaced by Halanx customer class
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def name(self):
        return self.user.get_full_name()



class Tenant(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    parent_name = models.CharField(max_length=50,null=True,blank=True)
    parent_phone = models.CharField(max_length=50,null=True,blank=True)
    parmenant_address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    pin = models.CharField(max_length=10,null=True,blank=True)
    country = models.CharField(max_length=15,null=True,blank=True)
    vehicle = models.BooleanField(default=False)
    total_balance = models.FloatField()

    # emergency contact
    emergeny_contact_name = models.CharField(max_length=50,null=True,blank=True)
    emergeny_contact_relation = models.CharField(max_length=50,null=True,blank=True)
    emergeny_contact_email = models.CharField(max_length=50,null=True,blank=True)
    emergeny_contact_phone = models.CharField(max_length=50,null=True,blank=True)

    #company contact
    company_name = models.CharField(max_length=50,null=True,blank=True)
    company_phone = models.CharField(max_length=50,null=True,blank=True)
    company_address = models.CharField(max_length=50,null=True,blank=True)
    company_email = models.CharField(max_length=50,null=True,blank=True)
    company_city= models.CharField(max_length=50,null=True,blank=True)
    company_state= models.CharField(max_length=50,null=True,blank=True)
    company_pin_code = models.CharField(max_length=50,null=True,blank=True)
    company_country = models.CharField(max_length=50,null=True,blank=True)

    work_start_date = models.DateField()
    work_end_date = models.DateField()



class Document(models.Model):
    tenant = models.ForeignKey('Tenant', related_name='shopper_documents', on_delete=models.CASCADE)
    type = models.CharField(max_length=30,null=True,choices=DocumentType)
    image = models.ImageField(upload_to=upload_documents,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tenant.user.phone)

class Transaction(models.Model):
    tenant = models.ForeignKey(Tenant)
    type = models.CharField(choices=TransactionType)
    amount = models.FloatField()
    total = models.FloatField()
    update = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)



