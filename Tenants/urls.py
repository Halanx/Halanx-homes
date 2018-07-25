from django.conf.urls import url
from HomeBooking.api import views

urlpatterns = [

    url(r'^detail/(?P<room_type>[-\w]+)/(?P<room_id>[0-9]+)/$', views.BookingdetailView.as_view()),
    url(r'^$',views.BookingListCreateView.as_view())
]
