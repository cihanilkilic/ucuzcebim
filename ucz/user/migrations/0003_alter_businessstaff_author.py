# Generated by Django 4.2 on 2023-05-01 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_businessstaff_mobile_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessstaff',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı Adı'),
        ),
    ]
