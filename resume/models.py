from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    experience = models.TextField()
    skills = models.TextField()
    about = models.TextField()

    photo = models.ImageField(upload_to='photos/')
    resume_file = models.FileField(upload_to='resume_files/')

    def __str__(self):
        return self.full_name