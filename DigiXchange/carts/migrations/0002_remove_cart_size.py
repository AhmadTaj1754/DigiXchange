# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-02 20:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='size',
        ),
    ]
