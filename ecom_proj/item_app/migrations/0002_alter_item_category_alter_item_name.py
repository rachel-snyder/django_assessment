# Generated by Django 5.0.3 on 2024-07-31 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]