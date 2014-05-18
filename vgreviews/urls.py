from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^', include('reviews.urls')),
    url(r'^reviews/', include('reviews.urls', namespace="reviews")),
    url(r'^admin/', include(admin.site.urls)),
)
