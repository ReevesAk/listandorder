# Generated by Django 4.2.1 on 2023-06-04 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=50)),
                ('business_CAC', models.CharField(max_length=100)),
                ('business_TIN', models.CharField(max_length=100)),
                ('nin', models.CharField(max_length=100)),
                ('bvn', models.CharField(max_length=100)),
                ('utility_bill', models.CharField(max_length=100)),
                ('Identification_no', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
