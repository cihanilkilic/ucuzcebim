# Generated by Django 4.2 on 2023-05-21 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=100, null=True, verbose_name='Ad-Soyad')),
                ('mail_address', models.CharField(max_length=50, null=True, verbose_name='Mail Adresi')),
                ('telephone', models.CharField(max_length=11, null=True, verbose_name='Telefon Numarası')),
                ('message', models.TextField(null=True, verbose_name='Mesajı')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Gönderilme Tarihi')),
            ],
        ),
    ]
