# Generated by Django 5.0.7 on 2024-08-20 20:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="duration",
            field=models.CharField(blank=True, default="", max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="synopsis",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]
