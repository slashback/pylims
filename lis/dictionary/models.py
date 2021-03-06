from django.db import models


class Biomaterial(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Division(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    name = models.CharField(max_length=64)
    division = models.ForeignKey(Division)

    def __str__(self):
        return self.name
