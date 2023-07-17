from django.db import models
from django.contrib.auth import models as models2
from datetime import datetime


class Year(models.Model):
    name = models.CharField(primary_key=True, max_length=10)


class Promo(models.Model):
    name = models.CharField(primary_key=True, max_length=10)
    first_year = models.ForeignKey(Year, on_delete=models.PROTECT)


class Student(models.Model):
    user = models.OneToOneField(models2.User(), on_delete=models.PROTECT)
    promo = models.ForeignKey(Promo, on_delete=models.PROTECT)


# TODO: Create a year model ?
class Gallery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, max_length=1000, unique=True)
    slug = models.SlugField(max_length=1000, blank=False, default="")
    description = models.CharField(max_length=10000)
    date = models.DateTimeField(blank=False, default=datetime.now)

    class Visibility(models.TextChoices):
        PUBLIC = "publique"
        SCHOOL = "école"
        PRIVATE = "privée"

    visibility = models.CharField(
        choices=Visibility.choices, default=Visibility.PRIVATE, max_length=10
    )

    class Type(models.TextChoices):
        PHOTO = "photo"
        VIDEO = "video"

    type = models.CharField(
        blank=False, default=Type.PHOTO, choices=Type.choices, max_length=10
    )
    year = models.ForeignKey(Year, on_delete=models.PROTECT, default=None)


class File(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(blank=False, max_length=1000)
    file_extension = models.CharField(blank=False, max_length=100)
    file_full_name = models.CharField(blank=False, max_length=1100)
    link = models.CharField(max_length=10000)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, default=None)


class Reaction(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Material(models.Model):
    name = models.CharField(max_length=1000)


"""
class Teams(models.Model):
    year = models.IntegerChoices(default=Student.Promotion.P25 ,choices=Student.Promotion.choices)
    members = models.onTo

"""
