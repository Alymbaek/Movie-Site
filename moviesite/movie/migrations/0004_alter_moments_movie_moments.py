# Generated by Django 5.1.1 on 2024-10-06 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_alter_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moments',
            name='movie_moments',
            field=models.ImageField(upload_to='movie_moments'),
        ),
    ]
