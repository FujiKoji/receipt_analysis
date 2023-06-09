# Generated by Django 4.1.5 on 2023-02-17 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PreventDentalPractice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "dental_practice_code",
                    models.IntegerField(
                        blank=True, default=None, null=True, verbose_name="歯科診療行為コード"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "予防診療行為コード",
                "db_table": "prevent_dental_practice",
            },
        ),
    ]
