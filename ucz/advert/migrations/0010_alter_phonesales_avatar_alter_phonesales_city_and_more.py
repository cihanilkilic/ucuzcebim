# Generated by Django 4.2 on 2023-05-09 01:16

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0009_alter_phonesales_memory_memory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonesales',
            name='avatar',
            field=models.FileField(null=True, upload_to='PhoneSales/', verbose_name='İlan Resmi'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='İl'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='district',
            field=models.CharField(max_length=100, null=True, verbose_name=' İlçe'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='garanti',
            field=models.CharField(default='Garantisi Yok', max_length=21, null=True, verbose_name='Garanti'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='label',
            field=models.CharField(default='Telefon-Satış', max_length=50, null=True, verbose_name='Etiket(Telefon Satış)'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='memory_memory',
            field=models.CharField(max_length=6, null=True, verbose_name='Telefon Hafıza Bellek'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='os',
            field=models.CharField(default='Android', max_length=8, null=True, verbose_name='Telefon İşletim Sistemi'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='phone_brand',
            field=models.CharField(max_length=250, null=True, verbose_name='Telefon Markası'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='phone_model',
            field=models.CharField(max_length=250, null=True, verbose_name='Telefon Modeli'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='price',
            field=models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='ram_memory',
            field=models.CharField(max_length=6, null=True, verbose_name='Telefon Ram Bellek'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='situation',
            field=models.CharField(default='İkinci El', max_length=10, null=True, verbose_name='Telefon Durumu'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='swap',
            field=models.CharField(max_length=6, null=True, verbose_name='Takas Durumu'),
        ),
    ]