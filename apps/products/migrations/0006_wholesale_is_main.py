# Generated by Django 4.2.4 on 2023-08-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_category_sub_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='wholesale',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
