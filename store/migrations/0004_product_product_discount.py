# Generated by Django 3.2.18 on 2023-03-22 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_discount',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
