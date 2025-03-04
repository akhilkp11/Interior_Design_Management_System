# Generated by Django 5.1.6 on 2025-03-03 15:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DesignApp', '0003_consultdb_status'),
        ('WebApp', '0006_rename_project_contactdb_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultdb',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebApp.userregistrationdb'),
        ),
    ]
