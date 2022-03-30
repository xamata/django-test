from django.db import models
from slugify import slugify
import os


def cover_directory_path(instance, filename):
    book_title = slugify(instance.name)
    _, extension = os.path.splitext(filename)
    return f"Companies/{book_title}{extension}"


# Create your models here.
class Book(models.Model):

    # Book model called in Schema, uses variables to fill in data
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=10)
    review = models.PositiveIntegerField()
    cover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to=cover_directory_path, blank=True)
