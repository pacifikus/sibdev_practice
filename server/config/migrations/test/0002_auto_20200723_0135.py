# Generated by Django 3.0.8 on 2020-07-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='random_string',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Рандомная строка'),
        ),
    ]
