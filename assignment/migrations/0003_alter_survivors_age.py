# Generated by Django 4.0.3 on 2022-03-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_survivors_infected_survivors_resources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survivors',
            name='age',
            field=models.IntegerField(max_length=50),
        ),
    ]