# Generated by Django 3.2.9 on 2022-08-05 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_auto_20220805_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='categary',
        ),
    ]
