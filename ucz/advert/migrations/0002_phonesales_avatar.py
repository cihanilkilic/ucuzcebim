# Generated by Django 4.2 on 2023-05-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonesales',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='adverts/PhoneSales/'),
        ),
    ]
