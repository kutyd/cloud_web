# Generated by Django 5.0.3 on 2024-05-09 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_web', '0003_rename_kisimail_kisi_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='kisi',
            name='KisiMail',
            field=models.CharField(default='xxx@gmail.com', max_length=50),
        ),
    ]
