from django.db import models
from django.utils import timezone

class Ecgwave(models.Model):
    timeunit = models.CharField(max_length=15)
    voltageunit = models.CharField(max_length=15)
    #time = models.SeparatedValuesField()
    #voltage = models.SeparatedValuesField()

    #def show()


    #def readvalue()


class File(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    #def save()


    #def delete()
