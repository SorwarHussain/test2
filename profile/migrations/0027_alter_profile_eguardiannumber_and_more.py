# Generated by Django 4.0.3 on 2022-06-27 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0026_alter_profile_elpdistrict_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='eguardianNumber',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='eguardianRelation',
            field=models.CharField(max_length=150),
        ),
    ]
