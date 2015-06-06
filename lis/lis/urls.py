from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'journal.views.home', name='home'),
    url(r'^specimen/(\d+)/', 'journal.views.specimen_info',
        name='specimen_info'),
    url(r'^journal/', include('journal.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
