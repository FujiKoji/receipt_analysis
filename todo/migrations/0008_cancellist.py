# Generated by Django 4.1.5 on 2023-03-22 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0007_remove_practicerecord_responsible_person_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CancelList",
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
                    "calte_num",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=255,
                        null=True,
                        verbose_name="カルテ番号",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        default="",
                        max_length=255,
                        null=True,
                        verbose_name="患者名",
                    ),
                ),
                (
                    "booking_num",
                    models.IntegerField(
                        blank=True, default=None, null=True, verbose_name="予約件数"
                    ),
                ),
                (
                    "without_permission",
                    models.IntegerField(
                        blank=True, default=None, null=True, verbose_name="無断"
                    ),
                ),
                (
                    "appointed_day",
                    models.IntegerField(
                        blank=True, default=None, null=True, verbose_name="当日"
                    ),
                ),
                (
                    "common",
                    models.IntegerField(
                        blank=True, default=None, null=True, verbose_name="通常"
                    ),
                ),
                (
                    "cancel_per",
                    models.IntegerField(
                        blank=True, default=None, null=True, verbose_name="キャンセル率"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "予約表",
                "db_table": "cancel_per",
            },
        ),
    ]
