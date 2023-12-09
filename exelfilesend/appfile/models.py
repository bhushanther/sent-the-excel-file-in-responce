from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    roll=models.CharField(max_length=50)
    city=models.CharField(max_length=50)


    def __str__(self):
        return self.first_name
