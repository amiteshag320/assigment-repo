# Generated by Django 4.0 on 2021-12-21 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.CharField(max_length=300),
        ),
    ]