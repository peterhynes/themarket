# Generated by Django 2.0.6 on 2018-07-30 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]