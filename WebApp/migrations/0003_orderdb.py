# Generated by Django 5.1.6 on 2025-02-14 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0002_cartdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Address', models.CharField(blank=True, max_length=200, null=True)),
                ('ShippingAddress', models.CharField(blank=True, max_length=200, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('Pin', models.IntegerField(blank=True, null=True)),
                ('TotalPrice', models.IntegerField(blank=True, null=True)),
                ('Message', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
