# Generated by Django 2.0.6 on 2018-07-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180725_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='retailer',
            field=models.BooleanField(default=False),
        ),
    ]
