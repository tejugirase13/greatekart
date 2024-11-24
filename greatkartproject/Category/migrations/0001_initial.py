# Generated by Django 5.1.1 on 2024-11-12 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('cat_image', models.ImageField(blank=True, upload_to='photos/categories')),
            ],
        ),
    ]
