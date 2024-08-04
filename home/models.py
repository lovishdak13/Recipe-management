from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=100,null=True)
    lname = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    branch = models.CharField(max_length=200,null=True)
    year = models.IntegerField(null=True)

    

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    car_speed=models.CharField(max_length=100)
    
    def __str__(self)->str:
        return self.car_name

