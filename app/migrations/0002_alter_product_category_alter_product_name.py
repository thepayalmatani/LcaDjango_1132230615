# Generated by Django 5.0.7 on 2024-09-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(verbose_name=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(verbose_name=100),
        ),
    ]