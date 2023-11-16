# Generated by Django 4.2.5 on 2023-11-16 17:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_username', models.CharField(max_length=30)),
                ('restaurant', models.CharField(max_length=30)),
                ('cost', models.CharField(max_length=30)),
                ('queueMan_username', models.CharField(max_length=30)),
                ('date', models.DateTimeField()),
                ('number_Queue', models.CharField(max_length=30)),
                ('number_of_customer', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('cancel_by_queueman', models.BooleanField(default=False)),
                ('cancel_by_user', models.BooleanField(default=False)),
                ('update_status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queueman_username', models.CharField(max_length=30)),
                ('customer_username', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=500)),
                ('star', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('type', models.ImageField(default=None, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(max_length=30)),
                ('number_of_customer', models.CharField(max_length=30)),
                ('customer_username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
