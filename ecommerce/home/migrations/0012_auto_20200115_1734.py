# Generated by Django 3.0.2 on 2020-01-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200115_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blogdescription_para2',
            field=models.TextField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='blogdescription_para3',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
