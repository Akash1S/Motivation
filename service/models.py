from django.db import models


class Course_Details(models.Model):
    c_name = models.CharField(max_length=50)
    c_faculty_name = models.CharField(max_length=50)
    c_duration = models.IntegerField()
    c_stating_date = models.DateField(default=True)


class Query_base(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Message = models.TextField(max_length=500)
    Mobile = models.IntegerField()
