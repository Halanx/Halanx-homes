from django.db import models
from django.conf import settings

from Common.utils import DocumentTypeCategories


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


class Document(models.Model):
    type = models.CharField(max_length=30, choices=DocumentTypeCategories)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class BankDetail(models.Model):
    account_holder_name = models.CharField(max_length=200, blank=True, null=True)
    account_number = models.CharField(max_length=50, blank=True, null=True)
    account_type = models.CharField(max_length=10, blank=True, null=True)
    bank_name = models.CharField(max_length=200, blank=True, null=True)
    bank_branch = models.CharField(max_length=300, blank=True, null=True)
    bank_branch_address = models.CharField(max_length=300, blank=True, null=True)
    ifsc_code = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)


class AddressDetail(models.Model):
    street_address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    pincode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)
