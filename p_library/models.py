from django.db import models
import os
from django.contrib.auth.models import User  

class UserProfile(models.Model):  
  
    age = models.PositiveIntegerField(null=True) 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


# Добавляем модель издательства
class Publisher(models.Model):
    publisher_name = models.TextField()

    def __str__(self):
        return self.publisher_name


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="book_author")
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    publisher = models.ForeignKey(Publisher, on_delete = models.CASCADE, null=True, related_name="publisher")
    image = models.ImageField(upload_to='media/books_photo', blank=True)

    def __str__(self):
        return self.title

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url


class Friend(models.Model):
    full_name = models.TextField()
    book = models.ManyToManyField(Book, related_name='book')

    def __str__(self):
        return self.full_name

