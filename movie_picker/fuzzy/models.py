# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Movies(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=5, decimal_places=1, blank=True)
    color = models.CharField(max_length=16, blank=True, null=True)
    director_name = models.CharField(max_length=32, blank=True, null=True)
    num_critic_for_reviews = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    duration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    director_facebook_likes = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    actor_3_facebook_likes = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    actor_2_name = models.CharField(max_length=28, blank=True, null=True)
    actor_1_facebook_likes = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    gross = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    genres = models.CharField(max_length=64, blank=True, null=True)
    actor_1_name = models.CharField(max_length=27, blank=True, null=True)
    movie_title = models.CharField(max_length=88, blank=True, null=True)
    num_voted_users = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)
    cast_total_facebook_likes = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    actor_3_name = models.CharField(max_length=30, blank=True, null=True)
    facenumber_in_poster = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    plot_keywords = models.CharField(max_length=149, blank=True, null=True)
    movie_imdb_link = models.CharField(max_length=52, blank=True, null=True)
    num_user_for_reviews = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    content_rating = models.CharField(max_length=9, blank=True, null=True)
    budget = models.DecimalField(max_digits=12, decimal_places=1, blank=True, null=True)
    title_year = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    actor_2_facebook_likes = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    imdb_score = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    aspect_ratio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    movie_facebook_likes = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movies'
