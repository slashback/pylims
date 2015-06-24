from django.db import models
from dictionary.models import Biomaterial, Measurement, Division


class Patient(models.Model):
    GENDER_FEMALE = 0
    GENDER_MALE = 1
    GENDER_UNDEFINED = 2
    GENDER_LIST = (
        (GENDER_FEMALE, 'Жен.'),
        (GENDER_MALE, 'Муж'),
        (GENDER_UNDEFINED, 'Не указано'),
    )
    last_name = models.CharField(default='', max_length=64)
    first_name = models.CharField(default='', max_length=64)
    middle_name = models.CharField(default='', max_length=64)
    gender = models.IntegerField(choices=GENDER_LIST, default=GENDER_UNDEFINED)
    birth_date = models.DateField()

    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)


class Application(models.Model):
    internal_nr = models.CharField(max_length=64)
    state = models.IntegerField()
    patient = models.ForeignKey(Patient)
    registration_date = models.DateField()

    def __str__(self):
        return self.internal_nr


class Specimen(models.Model):
    internal_nr = models.CharField(max_length=64)
    application = models.ForeignKey(Application)
    biomaterial = models.ForeignKey(Biomaterial)
    state = models.IntegerField()
    division = models.ForeignKey(Division)

    def __str__(self):
        return self.internal_nr


class MeasurementResult(models.Model):
    specimen = models.ForeignKey(Specimen)
    measurement = models.ForeignKey(Measurement)
    state = models.IntegerField()
    value = models.CharField(default='', max_length=64)

    def __str__(self):
        return self.values
