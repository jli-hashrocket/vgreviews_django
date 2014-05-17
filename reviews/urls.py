from django.conf.urls import patterns, url

from reviews import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^reviews/$', views.ReviewList.as_view(), name='review_list'),
    url(r'^new/$', views.ReviewCreate.as_view(), name='new'),
    url(r'^(?P<pk>\d+)/$', views.ReviewDetail.as_view(), name='show'),
    url(r'^edit/(?P<pk>\d+)/$', views.ReviewUpdate.as_view(), name='edit'),
)

