# Generated by Django 2.1.4 on 2019-01-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('dong', models.CharField(primary_key=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('medical', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=100)),
            ],
        ),
    ]