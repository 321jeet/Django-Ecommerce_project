# Generated by Django 3.2.9 on 2022-08-30 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0021_auto_20220830_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
