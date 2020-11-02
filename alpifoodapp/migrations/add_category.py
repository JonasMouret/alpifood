# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-11-01 22:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpifoodapp', '0003_order_orderdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.IntegerField(choices=[(1, 'Starter'), (2, 'Main course'), (3, 'Dessert')], default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.IntegerField(choices=[(1, 'Pizza'), (2, 'Savoyard'), (3, 'Meat'), (4, 'Fast-food'), (5, 'Gastro'), (6, 'Fast-food'), (7, 'Fast-food'), (8, 'Fast-food'), (9, 'Fast-food'), (10, 'Fast-food'), (11, 'Fast-food'), (12, 'Fast-food'), (13, 'Fast-food'), (14, 'Fast-food'), (15, 'Fast-food'), (16, 'Fast-food')], default=0),
        ),
    ]