# Generated by Django 3.2.9 on 2022-08-20 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0013_remove_customer_reat_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
