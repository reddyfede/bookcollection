# Generated by Django 4.2.5 on 2023-09-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(to='main_app.genre'),
        ),
    ]
