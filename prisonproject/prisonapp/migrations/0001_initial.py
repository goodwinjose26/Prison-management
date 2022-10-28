# Generated by Django 4.0.6 on 2022-10-03 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cellno', models.CharField(max_length=100)),
                ('capacity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prisoner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('dob', models.DateField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vdate', models.DateField()),
                ('vtime', models.CharField(max_length=100)),
                ('visitorname', models.CharField(max_length=100)),
                ('relation', models.CharField(max_length=100)),
                ('purpose', models.CharField(max_length=100)),
                ('carry', models.CharField(max_length=100)),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisonapp.prisoner')),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reldate', models.DateField()),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisonapp.prisoner')),
            ],
        ),
        migrations.CreateModel(
            name='Police',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisonapp.designation')),
            ],
        ),
        migrations.CreateModel(
            name='Parole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdate', models.DateField()),
                ('outtime', models.CharField(max_length=100)),
                ('days', models.IntegerField()),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisonapp.prisoner')),
            ],
        ),
        migrations.CreateModel(
            name='InOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outdate', models.DateField()),
                ('outtime', models.CharField(max_length=100)),
                ('inDate', models.DateField()),
                ('inTime', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisonapp.prisoner')),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crimedate', models.DateField()),
                ('crimetime', models.CharField(max_length=100)),
                ('hearingdate', models.DateField()),
                ('punishment', models.CharField(max_length=100)),
                ('crimestatus', models.CharField(max_length=100)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisonapp.cell')),
                ('prisoner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prisonapp.prisoner')),
            ],
        ),
    ]
