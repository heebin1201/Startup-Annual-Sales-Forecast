# Generated by Django 4.2.3 on 2023-08-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="project",
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
                ("money", models.IntegerField()),
                ("moneya", models.IntegerField()),
                ("moneyb", models.IntegerField()),
                ("moneyc", models.IntegerField()),
                ("employee", models.IntegerField()),
            ],
        ),
    ]
