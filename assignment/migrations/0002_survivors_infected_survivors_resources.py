# Generated by Django 4.0.3 on 2022-03-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survivors',
            name='infected',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='survivors',
            name='resources',
            field=models.JSONField(default=None),
        ),
    ]