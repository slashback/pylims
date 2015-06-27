from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'journal.views.registration_journal', name='home'),
    url(r'^specimen/(\d+)/', 'journal.views.specimen_info',
        name='specimen_info'),
    url(r'^specimen/save/(\d+)/', 'journal.views.specimen_save',
        name='specimen_save'),
    url(r'^journal/', include('journal.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
