# Generated by Django 3.0.2 on 2020-01-18 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descrpition', models.TextField()),
                ('technology', models.CharField(max_length=200)),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]
