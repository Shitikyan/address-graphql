# Generated by Django 4.1.3 on 2022-11-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("opendata", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="nycbuilding",
            name="building_city",
            field=models.CharField(default="NYC", max_length=255),
        ),
        migrations.AddField(
            model_name="nycbuilding",
            name="gross_sqft",
            field=models.CharField(default="-", max_length=255),
        ),
        migrations.AddField(
            model_name="nycbuilding",
            name="owner",
            field=models.CharField(default="-", max_length=255),
        ),
        migrations.AddField(
            model_name="nycbuilding",
            name="pytaxclass",
            field=models.CharField(default="-", max_length=255),
        ),
        migrations.AddField(
            model_name="nycbuilding",
            name="state",
            field=models.CharField(default="NY", max_length=255),
        ),
        migrations.AddField(
            model_name="nycbuilding",
            name="yrbuilt",
            field=models.IntegerField(default=-1, max_length=255),
        ),
    ]
