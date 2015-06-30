from django.contrib import admin
from journal.models import Application, Patient, Specimen, MeasurementResult

models = [Application, Patient, Specimen, MeasurementResult]
admin.site.register(models)
