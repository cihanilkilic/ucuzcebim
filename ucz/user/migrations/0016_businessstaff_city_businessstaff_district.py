# Generated by Django 4.2 on 2023-05-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_businessstaff_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessstaff',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='İl'),
        ),
        migrations.AddField(
            model_name='businessstaff',
            name='district',
            field=models.CharField(max_length=100, null=True, verbose_name=' İlçe'),
        ),
    ]
