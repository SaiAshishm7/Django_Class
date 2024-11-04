from django.db import models

class BMIRecord(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField()
    date_calculated = models.DateTimeField(auto_now_add=True)

    def calculate_bmi(self):
        height_in_meters = self.height / 100  # Convert cm to meters
        self.bmi = round(self.weight / (height_in_meters ** 2), 2)
        return self.bmi