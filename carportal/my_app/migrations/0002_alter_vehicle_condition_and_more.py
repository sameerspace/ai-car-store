# Generated by Django 4.0.4 on 2022-06-01 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='condition',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='displacement_cc',
            field=models.IntegerField(max_length=1000),
        ),
    ]
