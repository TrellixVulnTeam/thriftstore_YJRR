# Generated by Django 3.0.7 on 2020-06-10 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discounted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='picLink',
            field=models.URLField(max_length=700),
        ),
    ]
