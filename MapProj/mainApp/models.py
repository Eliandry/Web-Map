from django.db import models


class Country(models.Model):
    name = models.CharField("Название", max_length=100)
    photo = models.ImageField('обложка', upload_to='country/')


class Account(models.Model):
    name = models.CharField(max_length=30)
    ids = models.CharField(max_length=30)


class Trip(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city=models.CharField(max_length=50,blank=True)
    date=models.CharField(max_length=50)

class Impress(models.Model):
    trip = models.ForeignKey(Trip,on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    img = models.ImageField(upload_to="impress/")
    date = models.DateField()
