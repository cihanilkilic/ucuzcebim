# Generated by Django 4.2 on 2023-05-02 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_businessstaff_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessstaff',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
