# Generated by Django 4.2 on 2023-05-26 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_businessstaff_city_businessstaff_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessstaff',
            name='office_phone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='İş Telefonu'),
        ),
    ]
