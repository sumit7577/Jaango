# Generated by Django 3.2 on 2021-07-30 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='FullyFurnished',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
