from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required


from apps.reviews import views

urlpatterns = patterns('',
    url(r'^$', views.ReviewList.as_view(), name='review_list'),
    url(r'^new/$', login_required(views.ReviewCreate.as_view()), name='new'),
    url(r'^(?P<pk>\d+)/$', views.ReviewDetail.as_view(), name='show'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(views.ReviewUpdate.as_view()), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(views.ReviewDelete.as_view()), name='delete'),
    url(r'^like$', login_required(views.like), name='like'),

)

