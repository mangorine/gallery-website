from django.db import models
from django.contrib.auth import models as models2


class Student(models.Model):
    user = models.OneToOneField(models2.User(), on_delete=models.PROTECT)
    class Promotion(models.IntegerChoices):
        P25 = "025"
    promo = models.IntegerField(blank=False, default=Promotion.P25, choices=Promotion.choices)

class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False)
    description = models.CharField()
    date = models.DateField(blank=False)
    private = models.BooleanField(default=True)

    class Type(models.TextChoices):
        PHOTO = 'photo'
        VIDEO = 'video'
    
    type = models.CharField(blank=False, default=Type.PHOTO, choices=Type.choices)

class File(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(blank=False)
    file_extension = models.CharField(blank=False)
    file_full_name = models.CharField(blank=False)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)


class Reaction(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Material(models.Model):
    name = models.CharField()
    
"""
class Teams(models.Model):
    year = models.IntegerChoices(default=Student.Promotion.P25 ,choices=Student.Promotion.choices)
    members = models.onTo

"""