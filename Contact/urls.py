from django.conf.urls import url
from Contact.api import views

urlpatterns = [

    url(r'^submit/$',views.ContactformSubmittion)
]
