# Generated by Django 5.1.6 on 2025-02-18 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0007_designsdb_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='designsdb',
            name='Designer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
