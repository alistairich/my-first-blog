# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 17:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_for_electrical_post_for_electronics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post_for_Electronics',
            new_name='Electrical',
        ),
        migrations.RenameModel(
            old_name='Post_for_Electrical',
            new_name='Electronics',
        ),
    ]
