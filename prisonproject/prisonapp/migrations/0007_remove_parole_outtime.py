# Generated by Django 4.1.1 on 2022-10-07 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prisonapp', '0006_remove_inout_indate_remove_inout_intime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parole',
            name='outtime',
        ),
    ]
