# Generated by Django 3.2.9 on 2022-08-09 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0008_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='user_name',
            new_name='uname',
        ),
    ]
