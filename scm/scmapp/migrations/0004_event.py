# Generated by Django 4.0.6 on 2022-08-10 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0003_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=400)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
