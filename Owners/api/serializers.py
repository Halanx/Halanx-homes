from rest_framework import serializers

from Owners.models import Owner,Document,Transaction


class OwnerDetailSerializer(serializers.Serializer):
    class Meta:
        model = Owner
        fields = '__all__'

class OwnerDocumentSerializer(serializers.Serializer):
    class Meta:
        model = Document
        fields = ['img','type']

class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = Transaction
        fields = '__all__'

