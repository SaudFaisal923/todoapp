# Generated by Django 3.1.4 on 2021-01-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0002_auto_20210101_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='startdate',
            field=models.DateTimeField(),
        ),
    ]
