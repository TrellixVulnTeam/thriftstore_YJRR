# Generated by Django 3.0.7 on 2020-06-11 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200610_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
