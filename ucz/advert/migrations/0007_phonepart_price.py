# Generated by Django 4.2 on 2023-05-07 13:07

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0006_phonepart'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonepart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20),
        ),
    ]
