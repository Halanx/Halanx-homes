from django.conf.urls import url
from Homes.api import views

urlpatterns = (
    url(r'^houses/$', views.HouseListView.as_view()),
    url(r'^houses/(?P<pk>[0-9]+)/$', views.HouseRetrieveView.as_view()),
    url(r'^visits/$', views.HouseVisitListCreateView.as_view()),
    url(r'^visits/(?P<pk>[0-9]+)/$', views.HouseVisitRetrieveUpdateDeleteAPIView.as_view()),
)
