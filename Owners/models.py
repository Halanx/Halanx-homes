from django.db import models

from Common.models import AddressDetail, BankDetail, Document
from Owners.utils import get_owner_profile_pic_upload_path, get_owner_document_upload_path


class Owner(models.Model):
    customer = models.OneToOneField('Common.Customer', on_delete=models.PROTECT, related_name='house_owner')
    parent_name = models.CharField(max_length=50, null=True, blank=True)
    parent_phone_no = models.CharField(max_length=15, null=True, blank=True)

    address = models.OneToOneField('OwnerAddressDetail', null=True, on_delete=models.SET_NULL, related_name='owner')
    bank_detail = models.OneToOneField('OwnerBankDetail', null=True, on_delete=models.SET_NULL, related_name='owner')
    profile_pic = models.ImageField(upload_to=get_owner_profile_pic_upload_path, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    @property
    def name(self):
        return self.customer.name


class OwnerDocument(Document):
    owner = models.ForeignKey('Owner', null=True, on_delete=models.SET_NULL, related_name='documents')
    image = models.ImageField(upload_to=get_owner_document_upload_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            saved_image = self.image
            self.image = None
            super(OwnerDocument, self).save(*args, **kwargs)
            self.image = saved_image
            kwargs.pop('force_insert')
        super(OwnerDocument, self).save(*args, **kwargs)


class OwnerAddressDetail(AddressDetail):
    pass


class OwnerBankDetail(BankDetail):
    pass
