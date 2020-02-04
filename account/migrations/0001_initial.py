# Generated by Django 3.0.2 on 2020-02-03 10:41

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
            name='city',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=35)),
                ('CountryCode', models.CharField(max_length=3)),
                ('District', models.CharField(max_length=20)),
                ('Population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('Code', models.CharField(default='', max_length=3, primary_key=True, serialize=False)),
                ('Name', models.CharField(default='', max_length=52)),
                ('Continent', models.CharField(default='Asia', max_length=20)),
                ('Region', models.CharField(default='', max_length=26)),
                ('SurfaceArea', models.FloatField(default='0.00')),
                ('IndepYear', models.IntegerField(null=True)),
                ('Population', models.IntegerField(default='0', null=True)),
                ('LifeExpectancy', models.FloatField(null=True)),
                ('GNP', models.FloatField(null=True)),
                ('GNPOld', models.FloatField(null=True)),
                ('LocalName', models.CharField(max_length=45, null=True)),
                ('GovermentForm', models.CharField(max_length=45)),
                ('HeadOfState', models.CharField(max_length=60, null=True)),
                ('Capital', models.IntegerField(null=True)),
                ('Code2', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='countrylanguage',
            fields=[
                ('sl', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('CountryCode', models.CharField(max_length=3)),
                ('Language', models.CharField(max_length=30)),
                ('IsOfficial', models.CharField(choices=[('T', 'True'), ('F', 'False')], default='F', max_length=1)),
                ('Percentage', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('phone_number', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OTPUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(blank=True, max_length=6, null=True, verbose_name='OTP')),
                ('otp_last_generated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='otp', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
