# Generated by Django 3.1.7 on 2021-06-22 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listitapp', '0008_auto_20210622_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='users_list',
        ),
    ]
