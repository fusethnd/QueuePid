# Generated by Django 4.2.6 on 2023-11-15 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_alter_user_info_booking_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='booking_restaurant',
        ),
    ]
