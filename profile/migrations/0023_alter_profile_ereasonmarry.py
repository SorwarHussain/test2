# Generated by Django 4.0.3 on 2022-06-27 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0022_alter_profile_edhaknu_alter_profile_eislamicbook_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ereasonMarry',
            field=models.CharField(max_length=300),
        ),
    ]
