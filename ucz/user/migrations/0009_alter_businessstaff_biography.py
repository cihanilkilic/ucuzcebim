# Generated by Django 4.2 on 2023-05-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_remove_businessstaff_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessstaff',
            name='biography',
            field=models.TextField(blank=True, max_length=150, null=True, verbose_name='Biyografi'),
        ),
    ]
