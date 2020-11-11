# Generated by Django 2.2.17 on 2020-11-11 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=64, verbose_name='姓名')),
                ('deposit', models.FloatField(verbose_name='存款')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
