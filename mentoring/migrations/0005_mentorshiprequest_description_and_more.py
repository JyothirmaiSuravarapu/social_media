# Generated by Django 4.2 on 2023-04-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mentoring", "0004_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="mentorshiprequest",
            name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="mentorshiprequest",
            name="title",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="mentorshiprequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("PENDING", "Pending"),
                    ("ACCEPTED", "Accepted"),
                    ("REJECTED", "Rejected"),
                ],
                default="PENDING",
                max_length=10,
            ),
        ),
    ]
