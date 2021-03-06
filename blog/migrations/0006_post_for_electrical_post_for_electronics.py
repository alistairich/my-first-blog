# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 16:57
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20170803_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_for_Electrical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_for_Electronics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=200)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
