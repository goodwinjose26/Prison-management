# Generated by Django 4.1.1 on 2022-10-05 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prisonapp', '0003_rename_place_police_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='crime',
            name='crimedetails',
            field=models.CharField(default=0, max_length=500),
        ),
        migrations.AddField(
            model_name='crime',
            name='crimetitle',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
