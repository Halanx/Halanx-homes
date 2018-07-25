from rest_framework import serializers

from Tenants.models import Tenant,Document,Transaction


class TenantDetailSerializer(serializers.Serializer):
    class Meta:
        model = Tenant
        fields = '__all__'

class TenantDocumentSerializer(serializers.Serializer):
    class Meta:
        model = Document
        fields = ['img','type']

class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = Transaction
        fields = '__all__'

