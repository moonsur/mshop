from django.db import models
from django.utils import timezone


class Genre(models.Model):
    genre = models.CharField(max_length=255, null=True)


class Movie(models.Model):
    name = models.CharField(max_length=255, null=True)
    release_year = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    number_in_stock = models.IntegerField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
