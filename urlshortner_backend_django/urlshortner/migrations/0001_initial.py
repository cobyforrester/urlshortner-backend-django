# Generated by Django 3.0.8 on 2020-07-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.CharField(max_length=100)),
                ('shorturl', models.CharField(max_length=7)),
            ],
        ),
    ]