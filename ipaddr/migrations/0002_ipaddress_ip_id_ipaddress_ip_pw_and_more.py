# Generated by Django 4.2 on 2023-05-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ipaddr", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ipaddress",
            name="ip_id",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="ipaddress",
            name="ip_pw",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="ipaddress",
            name="hostname",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]