from django.db import models

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    summary = models.TextField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    graduation_date = models.DateField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=20)

    def __str__(self):
        return self.name