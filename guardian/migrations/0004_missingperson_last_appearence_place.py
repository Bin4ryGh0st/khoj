# Generated by Django 3.0.2 on 2020-02-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guardian', '0003_missingperson_blood_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='missingperson',
            name='last_appearence_place',
            field=models.TextField(blank=True, null=True),
        ),
    ]
