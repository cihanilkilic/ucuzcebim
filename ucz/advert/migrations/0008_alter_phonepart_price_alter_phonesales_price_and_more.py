# Generated by Django 4.2 on 2023-05-07 13:53

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advert', '0007_phonepart_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonepart',
            name='price',
            field=models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=20),
        ),
        migrations.AlterField(
            model_name='phonesales',
            name='price',
            field=models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=20),
        ),
        migrations.CreateModel(
            name='PhoneAksesuar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='İlan Aktif mi?')),
                ('label', models.CharField(blank=True, default='Telefon-Aksesuar', max_length=50, null=True, verbose_name='Telefon-Aksesuarı')),
                ('aksesuar_name', models.CharField(blank=True, max_length=110, null=True, verbose_name='Aksesuar Adı')),
                ('situation', models.CharField(blank=True, default='İkinci El', max_length=10, null=True, verbose_name='Aksesuar Durumu')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='İl')),
                ('district', models.CharField(blank=True, max_length=100, null=True, verbose_name=' İlçe')),
                ('price', models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=20)),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('avatar', models.FileField(blank=True, null=True, upload_to='PhoneAksesuar/', verbose_name='İlan Resmi')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Oluşturulma Tarihi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PhoneAksesuar', to=settings.AUTH_USER_MODEL, verbose_name='İlan Sahibi')),
            ],
        ),
    ]
