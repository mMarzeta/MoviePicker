from django.db import models


class Movie(models.Model):
    color = models.CharField(max_length=20,
                             choices=(('BW', 'Black and white'), ('CLR', 'COLOR'),),
                             default='CLR')
    director = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    duration = models.DecimalField(max_digits=4, decimal_places=1)
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1)
    year = models.IntegerField()


class Genre(models.Model):
    movie = models.ForeignKey(Movie)
    title = models.CharField(max_length=100)