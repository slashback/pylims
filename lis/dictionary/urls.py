from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^dictionary/',include('dictionary.urls'))
    url(r'^admin/', include(admin.site.urls)),
)
