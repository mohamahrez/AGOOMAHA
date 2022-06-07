# Generated by Django 3.2.9 on 2022-03-11 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agoon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='Student name')),
                ('schools', models.CharField(max_length=20, null=True, verbose_name='Student school')),
                ('clases', models.CharField(max_length=20, null=True, verbose_name='Student class')),
                ('s_points', models.TextField(max_length=600, verbose_name='Student points')),
                ('statues', models.CharField(max_length=60, verbose_name='passed or filed')),
                ('s_year', models.CharField(max_length=60, verbose_name='yearly school')),
                ('comment', models.TextField(max_length=1000, verbose_name='special needs')),
            ],
        ),
    ]
