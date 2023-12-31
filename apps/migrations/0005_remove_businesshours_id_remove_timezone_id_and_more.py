# Generated by Django 4.2.7 on 2023-11-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps", "0004_rename_store_id_businesshours_store_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="businesshours",
            name="id",
        ),
        migrations.RemoveField(
            model_name="timezone",
            name="id",
        ),
        migrations.AlterField(
            model_name="businesshours",
            name="store",
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="timezone",
            name="store",
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name="store",
            unique_together={("store", "timestamp_utc")},
        ),
    ]
