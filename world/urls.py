from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.suit_list, name='suit_list'),
    url(r'^suit/(?P<pk>[0-9]+)/$', views.suit_detail, name='suit_detail'),
    url(r'^suit/new/$', views.suit_new, name='suit_new'),
]