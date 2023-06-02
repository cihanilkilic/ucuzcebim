# Generated by Django 4.2 on 2023-04-30 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=True)),
                ('avatar', models.ImageField(blank=True, default='user/user_image_default/avatar.png', upload_to='user/user_images/')),
                ('website', models.URLField(blank=True, null=True)),
                ('biography', models.CharField(blank=True, max_length=150, null=True)),
                ('social_media', models.TextField(blank=True, null=True)),
                ('views', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Oluşturulma Tarihi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı Id')),
            ],
        ),
    ]
