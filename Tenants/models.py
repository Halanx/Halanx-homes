from django.db import models

from Common.models import Document, AddressDetail, BankDetail
from Tenants.utils import get_tenant_document_upload_path


class Tenant(models.Model):
    customer = models.OneToOneField('Common.Customer', on_delete=models.PROTECT, related_name='tenant')
    parent_name = models.CharField(max_length=50, null=True, blank=True)
    parent_phone_no = models.CharField(max_length=15, null=True, blank=True)
    permanent_address = models.OneToOneField('TenantAddressDetail', null=True, on_delete=models.SET_NULL,
                                             related_name='tenant')
    has_vehicle = models.BooleanField(default=False)

    # emergency contact
    emergency_contact_name = models.CharField(max_length=50, null=True, blank=True)
    emergency_contact_relation = models.CharField(max_length=50, null=True, blank=True)
    emergency_contact_email = models.CharField(max_length=50, null=True, blank=True)
    emergency_contact_phone_no = models.CharField(max_length=50, null=True, blank=True)

    # company contact
    company_name = models.CharField(max_length=50, null=True, blank=True)
    company_phone_no = models.CharField(max_length=50, null=True, blank=True)
    company_address = models.OneToOneField('TenantCompanyAddressDetail', null=True, on_delete=models.SET_NULL,
                                           related_name='tenant')

    def __str__(self):
        return str(self.id)

    @property
    def name(self):
        return self.customer.name


class TenantDocument(Document):
    tenant = models.ForeignKey('Tenant', null=True, on_delete=models.SET_NULL, related_name='documents')
    image = models.ImageField(upload_to=get_tenant_document_upload_path, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            saved_image = self.image
            self.image = None
            super(TenantDocument, self).save(*args, **kwargs)
            self.image = saved_image
            kwargs.pop('force_insert')
        super(TenantDocument, self).save(*args, **kwargs)


class TenantAddressDetail(AddressDetail):
    pass


class TenantCompanyAddressDetail(AddressDetail):
    pass
