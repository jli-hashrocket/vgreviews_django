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
    url(r'^consoles/ps4$', views.PS4ReviewList, name='ps4'),
    url(r'^consoles/xbox-one$', views.XboxOneReviewList, name='xbox-one'),
    url(r'^consoles/nintendo-wii-u$', views.WiiUReviewList, name='nintendo-wii-u'),
    url(r'^consoles/pc$', views.PCReviewList, name='pc'),
    url(r'^consoles/ps-vita$', views.PSVitaReviewList, name='ps-vita'),
    url(r'^consoles/nintendo-ds$', views.DSReviewList, name='nintendo-ds'),

)

