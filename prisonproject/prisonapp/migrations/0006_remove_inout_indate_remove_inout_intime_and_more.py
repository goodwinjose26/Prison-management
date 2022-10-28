# Generated by Django 4.1.1 on 2022-10-07 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prisonapp', '0005_rename_cell_crime_cellno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inout',
            name='inDate',
        ),
        migrations.RemoveField(
            model_name='inout',
            name='inTime',
        ),
        migrations.RemoveField(
            model_name='inout',
            name='outdate',
        ),
        migrations.RemoveField(
            model_name='inout',
            name='outtime',
        ),
        migrations.AddField(
            model_name='inout',
            name='indatetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='inout',
            name='outdatetime',
            field=models.DateTimeField(null=True),
        ),
    ]