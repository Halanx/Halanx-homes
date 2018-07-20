from django.contrib import admin
from Contact.models import FormSubmission

@admin.register(FormSubmission)
class FormSubmitModelAdmin(admin.ModelAdmin):
	list_display = ['id','first_name','last_name', 'phone','email']

	class Meta:
		model = FormSubmission
