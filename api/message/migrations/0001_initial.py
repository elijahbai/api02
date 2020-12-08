# Generated by Django 2.2.17 on 2020-12-08 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=128, unique=True, verbose_name='消息')),
                ('user', models.TextField(blank=True, null=True, verbose_name='用户信息')),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]
