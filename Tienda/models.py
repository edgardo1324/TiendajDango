from django.db import models

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')

class Offer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='offers/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

class User(models.Model):
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=128)

class UserStore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
