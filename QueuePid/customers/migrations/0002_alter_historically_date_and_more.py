# Generated by Django 4.2.6 on 2023-11-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historically',
            name='date',
            field=models.DateField(max_length=30),
        ),
        migrations.AlterField(
            model_name='historically',
            name='phone_number_QueueMan',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='historically',
            name='phone_number_customer',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='historically',
            name='queeuManName',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='historically',
            name='restaurant',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='historically',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
