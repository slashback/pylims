from django.contrib import admin
from dictionary.models import Biomaterial, Measurement, Division

models = [Biomaterial, Measurement, Division]
admin.site.register(models)
