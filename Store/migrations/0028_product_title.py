# Generated by Django 3.2.9 on 2022-08-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0027_alter_productdetail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]