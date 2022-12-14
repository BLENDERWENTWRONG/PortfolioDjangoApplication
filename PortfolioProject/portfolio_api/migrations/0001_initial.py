# Generated by Django 4.1.3 on 2022-11-18 01:48

from django.db import migrations, models
import djongo.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('avatar', models.ImageField(height_field=128, storage=djongo.storage.GridFSStorage(base_url='myfiles/', collection='myfiles'), upload_to='users', width_field=128)),
                ('email', models.EmailField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('birthDate', models.DateField()),
            ],
        ),
    ]
