# Generated by Django 4.0.3 on 2022-05-26 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0004_alter_profile_estatusflag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='estatusFlag',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
