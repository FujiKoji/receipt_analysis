# Generated by Django 4.1.5 on 2023-03-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0008_cancellist"),
    ]

    operations = [
        migrations.AddField(
            model_name="cancellist",
            name="cancel_num",
            field=models.IntegerField(
                blank=True, default=None, null=True, verbose_name="キャンセル件数"
            ),
        ),
    ]
