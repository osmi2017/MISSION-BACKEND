# Generated by Django 3.2.9 on 2021-11-20 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20211120_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entite',
            name='logo',
            field=models.ImageField(upload_to='logo'),
        ),
    ]
