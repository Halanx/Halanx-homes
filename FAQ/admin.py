from django.contrib import admin
from FAQ.models import Topic, Question

class TopicModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'name', 'slug']

	class Meta:
		model = Topic


class QuestionModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'text', 'topic', 'created_on']
	prepopulated_fields = {'slug':('text',)}
	list_filter = ['topic']

	class Meta:
		model = Question

admin.site.register(Topic, TopicModelAdmin)
admin.site.register(Question, QuestionModelAdmin)