# Generated by Django 3.0.6 on 2020-07-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roundtrip', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('country1', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=50)),
                ('retu', models.CharField(max_length=50)),
                ('adult', models.CharField(max_length=50)),
                ('child', models.CharField(max_length=50)),
                ('travel', models.CharField(max_length=50)),
            ],
        ),
    ]
