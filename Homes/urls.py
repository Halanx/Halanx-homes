from django.conf.urls import url
from Homes.api import views

urlpatterns = [

    url(r'^$', views.getAllHomes), # get all homes detail
    url(r'^house/(?P<pk>[0-9]+)/$', views.getParticularHome),   # get particular house details
    url(r'^placevisit/$', views.postHouseVisit),   # post a visit to house
    url(r'^scheduled/$', views.getScheduledVisits),   # get scheduled visits
    url(r'^visited/$', views.getVisiteddVisits),   # get visited details
]
