# Generated by Django 5.1.6 on 2025-02-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, unique=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='Category Images')),
            ],
        ),
    ]
