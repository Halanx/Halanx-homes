from django.conf.urls import url
from Homes.api import views

urlpatterns = [

    url(r'^$', views.getAllHomes), # get all project details
    url(r'^house/(?P<pk>[0-9]+)/$', views.getParticularHome),   # get particular project details
    url(r'^placevisit/$', views.postHouseVisit),   # get particular project details
    url(r'^scheduled/$', views.getScheduledVisits),   # get particular project details
    url(r'^visited/$', views.getVisiteddVisits),   # get particular project details
]
