# Generated by Django 4.2.4 on 2023-08-23 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country', to='company.country'),
        ),
    ]
