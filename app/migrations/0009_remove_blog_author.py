# Generated by Django 5.0.7 on 2024-08-04 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
