from django.contrib import admin
from journal.models import Application, Patient, Specimen, MeasurementResult


admin.site.register(Application)
admin.site.register(Patient)
admin.site.register(Specimen)
admin.site.register(MeasurementResult)
