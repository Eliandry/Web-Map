from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField("Название", max_length=100)
    capital = models.CharField("Название", max_length=100,blank=True)
    part = models.CharField("Название", max_length=100,blank=True)
    population = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    popular=models.IntegerField(default=0)
    grade=models.FloatField(default=0)
    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=30)
    ids = models.CharField(max_length=30)


class Trip(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, blank=True)
    date = models.CharField(max_length=50)
    grade=models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(10)])

class Impress(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    img = models.ImageField(upload_to="impress/")
    date = models.DateField()
