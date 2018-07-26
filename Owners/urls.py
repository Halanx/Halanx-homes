from django.conf.urls import url
from Owners.api import views

urlpatterns = [

    url(r'^document/$', views.DocumentListCreate.as_view())
]
