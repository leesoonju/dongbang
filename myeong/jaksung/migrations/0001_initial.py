# Generated by Django 2.2.1 on 2019-05-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('writer', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
