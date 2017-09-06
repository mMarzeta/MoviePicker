# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-06 17:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('BW', 'Black and white'), ('CLR', 'COLOR')], default='CLR', max_length=20)),
                ('director', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('duration', models.DecimalField(decimal_places=1, max_digits=4)),
                ('imdb_score', models.DecimalField(decimal_places=1, max_digits=3)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='genre',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fuzzy.Movie'),
        ),
    ]