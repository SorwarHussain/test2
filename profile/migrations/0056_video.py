# Generated by Django 4.0.3 on 2023-02-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0055_instructor_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('Video', models.FileField(upload_to='video/%y')),
            ],
        ),
    ]