# Generated by Django 5.0.6 on 2024-06-17 01:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_delete_movieinfo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='Movieinfo',
        ),
    ]
