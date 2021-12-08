from django.db import models
from django.db.models.fields import CharField

class Pet(models.Model):
    SEX_CHOICE = [('M', 'Male'),('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    descroption = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICE, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)
class vaccine(models.Model):
    name = models.CharField(max_length=50)
    