# Generated by Django 5.1.6 on 2025-02-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_productdb_sub_category_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
