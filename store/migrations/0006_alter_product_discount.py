# Generated by Django 3.2.18 on 2023-03-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20230322_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, default=14),
        ),
    ]
