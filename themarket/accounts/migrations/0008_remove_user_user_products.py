# Generated by Django 2.0.6 on 2018-07-30 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_products',
        ),
    ]