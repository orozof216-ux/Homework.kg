from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.IntegerField()
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    published_date = models.DateField()
    cover = models.ImageField(upload_to='books/')
    file = models.FileField(upload_to='books/files/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title