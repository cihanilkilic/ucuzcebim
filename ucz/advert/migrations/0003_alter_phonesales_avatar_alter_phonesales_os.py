# Generated by Django 4.2 on 2023-05-06 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0002_phonesales_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonesales',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='PhoneSales/', verbose_name='İlan Resmi'),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='os',
            field=models.CharField(blank=True, default='Android', max_length=8, null=True, verbose_name='Telefon İşletim Sistemi'),
        ),
    ]
