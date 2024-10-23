from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.CharField(max_length=20)  
    
    def __str__(self):
        return f"{self.name} - {self.rollno}"