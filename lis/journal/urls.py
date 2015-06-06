from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^patients/','journal.views.patients_journal', name='patients_journal'),
    url(r'^admin/', include(admin.site.urls)),
)
