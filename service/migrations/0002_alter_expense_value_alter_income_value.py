# Generated by Django 4.1.3 on 2022-12-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='value',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='value',
            field=models.IntegerField(default=0, null=True),
        ),
    ]