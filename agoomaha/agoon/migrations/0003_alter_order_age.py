# Generated by Django 3.2.9 on 2022-03-11 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agoon', '0002_studentreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='age',
            field=models.IntegerField(max_length=60, verbose_name='student age'),
        ),
    ]
