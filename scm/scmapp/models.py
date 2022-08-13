from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    gender=models.CharField(max_length=10)
    password=models.CharField(max_length=200)
    contact=models.CharField(max_length=12)


    def __str__(self):
        return self.name

class Book_ground(models.Model):
    bid=models.AutoField(primary_key=True)
    uid=models.IntegerField()
    name=models.CharField(max_length=200)
    date=models.DateField()
    time=models.TimeField()
    mobile=models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Admin(models.Model):
    aid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    eid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=400)
    date=models.DateField()
    time=models.TimeField()
    duration=models.IntegerField()

    def __str__(self):
        return self.name