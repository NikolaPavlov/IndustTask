# Generated by Django 3.0 on 2019-12-08 13:05

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, unique=True)),
                ('currency_abbr', models.CharField(max_length=200, unique=True)),
                ('rate_vs_base', models.DecimalField(decimal_places=6, max_digits=20, validators=[django.core.validators.MinValueValidator(Decimal('0.000001'))])),
            ],
            options={
                'verbose_name_plural': 'currencies',
                'ordering': ('currency_abbr',),
            },
        ),
    ]
