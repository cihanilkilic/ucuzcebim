# Generated by Django 4.2 on 2023-05-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0014_mobilerepair_jobfinish'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilerepair',
            name='acceptance',
            field=models.BooleanField(default=False, verbose_name='İstek Onaylı Mı?'),
        ),
    ]
