# Generated by Django 5.1.6 on 2025-02-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_contactdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdb',
            name='Project',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
