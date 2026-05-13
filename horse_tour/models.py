from django.db import models
from django.core.exceptions import ValidationError


class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Horse(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.owner}"


class TourCompany(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    companies = models.ManyToManyField(TourCompany)

    def __str__(self):
        return self.name


class Review(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(TourCompany, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    text = models.TextField()

    def clean(self):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError("Оценка только от 1 до 5")

    def __str__(self):
        return f"{self.person} - {self.company}"


class Booking(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    company = models.ForeignKey(TourCompany, on_delete=models.CASCADE)
    date = models.DateField()
    people_count = models.IntegerField()

    def __str__(self):
        return f"{self.person} - {self.company}"