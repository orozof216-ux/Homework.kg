from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    date = models.DateField()
    people_count = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.company}"