# Generated by Django 5.1.6 on 2025-02-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0006_designcategorydb_designsdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='designsdb',
            name='Category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
