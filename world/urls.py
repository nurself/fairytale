from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns = [
    url(r'^$', views.agreement_list, name='agreement_list'),
    url(r'^suit/(?P<pk>[0-9]+)/$', views.suit_detail, name='suit_detail'),
    url(r'^suit/new/$', views.suit_new, name='suit_new'),
    url(r'^suit/(?P<pk>[0-9]+)/edit/$', views.suit_edit, name='suit_edit'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),

    url(r'^agreement/(?P<pk>[0-9]+)/$', views.agreement_detail, name='agreement_detail'),
]