# Generated by Django 4.1.1 on 2022-10-05 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prisonapp', '0002_rename_cell_cells'),
    ]

    operations = [
        migrations.RenameField(
            model_name='police',
            old_name='place',
            new_name='email',
        ),
    ]
