from rest_framework import serializers
from Contact.models import FormSubmission

class FormSubmitionSerializer(serializers.ModelSerializer):
	class Meta:
		model = FormSubmission
		fields = '__all__'

