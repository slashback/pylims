from django.db import models
from dictionary.models import Biomaterial, Measurement


class Patient(models.Model):
    last_name = models.CharField(default='', max_length=64)
    first_name = models.CharField(default='', max_length=64)
    middle_name = models.CharField(default='', max_length=64)
    gender = models.IntegerField()
    birth_date = models.DateField()
    def __str__(self):
        return self.last_name


class Application(models.Model):
    internal_nr = models.CharField(max_length=64)
    state = models.IntegerField()
    patient = models.ForeignKey('Patient')
    def __str__(self):
        return self.internal_nr


class Specimen(models.Model):
    internal_nr = models.CharField(max_length=64)
    application = models.ForeignKey('Application')
    biomaterial = models.ForeignKey(Biomaterial)
    state = models.IntegerField()
    def __str__(self):
        return self.internal_nr


class MeasurementResult(models.Model):
    specimen = models.ForeignKey('Specimen')
    measurement = models.ForeignKey(Measurement)
    state = models.IntegerField()
    value = models.CharField(max_length=64)
    def __str__(self):
        return self.value