# Generated by Django 3.0.2 on 2020-02-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200203_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
    ]