from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^patients/', 'journal.views.patients_journal', name='patients_journal'),
    url(r'^applications/', 'journal.views.registration_journal', name='registration_journal'),
    url(r'^application/form$', 'journal.views.application_form', name='application_form'),
    url(r'^application/add$', 'journal.views.create_application', name='create_application'),
    url(r'^(\d+)/', 'journal.views.work_journal', name='work_journal'),
    url(r'^admin/', include(admin.site.urls)),
)
