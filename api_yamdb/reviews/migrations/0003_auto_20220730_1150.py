# Generated by Django 2.2.16 on 2022-07-30 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220728_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=300, verbose_name='Биография'),
        ),
    ]