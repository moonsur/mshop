# Generated by Django 2.2.13 on 2020-07-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='reveiw',
            field=models.FloatField(null=True),
        ),
    ]
