# Generated by Django 4.2 on 2023-05-26 22:07

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0015_mobilerepair_acceptance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonesales',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True),
        ),
    ]
