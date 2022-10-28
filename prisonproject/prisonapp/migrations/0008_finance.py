# Generated by Django 4.1.1 on 2022-10-15 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prisonapp', '0007_remove_parole_outtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisonapp.release')),
            ],
        ),
    ]