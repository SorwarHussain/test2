# Generated by Django 4.0.3 on 2022-11-17 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0044_remove_profile_district_remove_profile_upazila_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('course_type', models.CharField(choices=[('shortCourse', 'shortCourse'), ('longCourse', 'longCourse')], default='shortCourse', max_length=20)),
                ('course_status', models.CharField(choices=[('shortCourse', 'shortCourse'), ('longCourse', 'longCourse')], default='shortCourse', max_length=20)),
                ('instructor', models.TextField()),
                ('fee', models.IntegerField()),
                ('enroled', models.IntegerField()),
                ('shortDescription', models.TextField()),
                ('aboutCourse', models.TextField()),
                ('whatLearn', models.TextField()),
                ('forWhome', models.TextField()),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
