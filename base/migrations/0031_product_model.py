# Generated by Django 4.0.1 on 2022-01-30 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0030_brand_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
