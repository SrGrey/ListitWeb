# Generated by Django 3.1.7 on 2021-06-22 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listitapp', '0007_auto_20210622_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users_list',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listitapp.users_list', verbose_name='Users_List'),
        ),
    ]
