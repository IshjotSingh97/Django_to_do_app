# Generated by Django 3.0.2 on 2020-02-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todotitle',
            field=models.CharField(max_length=255),
        ),
    ]
