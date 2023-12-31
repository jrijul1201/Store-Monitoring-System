# Generated by Django 4.2.7 on 2023-11-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "apps",
            "0010_delete_storereport_rename_data_report_store_data_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="timezone",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="businesshours",
            name="store",
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name="store",
            name="store",
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name="store",
            name="timestamp_utc",
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name="timezone",
            name="store",
            field=models.IntegerField(db_index=True),
        ),
    ]
