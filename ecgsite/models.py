from django.db import models
from django.utils import timezone



class File(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    timeunit = models.CharField(max_length=15, default='s')
    voltageunit = models.CharField(max_length=15, default='mV')

    #time = models.SeparatedValuesField()
    #voltage = models.SeparatedValuesField()

    #def show()


    #def readvalue()


class Point(models.Model):
    time = models.FloatField()
    value = models.FloatField()
    wave = models.ForeignKey(File, on_delete=models.CASCADE)
