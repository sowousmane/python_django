# Generated by Django 3.2.3 on 2021-05-27 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_customer_order_ordereditem_shippinngadress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
