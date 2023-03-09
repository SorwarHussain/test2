# Generated by Django 4.0.3 on 2022-05-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cRequestNo', models.IntegerField()),
                ('cname', models.CharField(max_length=100)),
                ('cemail', models.EmailField(max_length=100)),
                ('cnumber', models.CharField(max_length=100)),
                ('cbiodatano', models.CharField(max_length=300)),
                ('cbiodataintotal', models.CharField(choices=[('১', '১'), ('২', '২'), ('৩', '৩'), ('৪', '৪'), ('৫', '৫')], default='১', max_length=10)),
                ('camount', models.CharField(max_length=200)),
                ('cBkashNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('cBkashTransactionID', models.CharField(blank=True, max_length=200, null=True)),
                ('cRocketNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('cRocketTransactionID', models.CharField(blank=True, max_length=200, null=True)),
                ('cNagadNumber', models.CharField(blank=True, max_length=200, null=True)),
                ('cNagadTransactionID', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
