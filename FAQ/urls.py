from django.conf.urls import url
from FAQ.api import views

urlpatterns = [

    url(r'^(?P<topic__slug>[-\w]+)/(?P<slug>[-\w]+)/$', views.QuestionDetailView.as_view()), # get questions
    url(r'^(?P<slug>[-\w]+)/$', views.TopicDetailView.as_view()),   # get particular topic detail
    url(r'^$', views.TopicListView.as_view()),                      #get all topics\
    url(r'faq/(?P<slug>[-\w]+)/^$', views.QuestionListView.as_view())   #get all faq's for tenant/owner/other

]
