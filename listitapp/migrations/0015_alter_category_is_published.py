# Generated by Django 3.2.7 on 2021-10-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listitapp', '0014_auto_20211013_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Show'),
        ),
    ]
