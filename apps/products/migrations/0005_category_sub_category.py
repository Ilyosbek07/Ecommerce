# Generated by Django 4.2.4 on 2023-08-24 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_producttype_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extra_category', to='products.category'),
        ),
    ]
