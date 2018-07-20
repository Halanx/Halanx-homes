from django.db import models

Plan = (
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('None','None'),
)

Tenants = (
    ('Boys','Boys'),
    ('Girls','Girls'),
    ('Family','Family'),
    ('Any','Any'),
)

Occupancy = (
    ('Owner_Staying','Owner_Staying'),
    ('Tenant_Staying','Tenant_Staying'),
    ('Vacant','Vacant')
)

HouseTypeCategories = (
    ('Apartment', 'Apartment'),
    ('Independnet', 'Independnet'),
    ('Villa', 'Villa'),
)

FurnishTypeCategories = (
    ('Fully furnished', 'Fully furnished'),
    ('Semi furnished', 'Semi furnished'),
    ('Unfurnished', 'Unfurnished')
)


class FormSubmission(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200,null=True)
    plan = models.CharField(max_length=25, blank=True, null=True, choices=Plan)
    occupancy = models.CharField(max_length=25, blank=True, null=True, choices=Occupancy)
    bed_count = models.IntegerField(null=True,blank=True)
    furnish = models.CharField(max_length=25, blank=True, null=True, choices=FurnishTypeCategories)
    tenant_tyoe = models.CharField(max_length=25, blank=True, null=True, choices=Tenants)
    house_type = models.CharField(max_length=25, blank=True, null=True, choices=HouseTypeCategories)
    current_rent = models.IntegerField(null=True,blank=True)
    expected_rent = models.IntegerField(null=True,blank=True)
    current_secuirity_deposit = models.IntegerField(null=True,blank=True)
    expected_secuirity_deposit = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.pk)

