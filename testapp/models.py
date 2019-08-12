from django.db import models


class User_Model(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Father_Name = models.CharField(max_length=50)
    Email = models.EmailField(default=None)
    Mobile = models.PositiveIntegerField()
    State = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Qualification = models.CharField(max_length=50)
