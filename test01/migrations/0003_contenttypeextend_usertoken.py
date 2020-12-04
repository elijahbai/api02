# Generated by Django 2.2.17 on 2020-11-11 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('test01', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('expiretime', models.IntegerField(verbose_name='到期时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test01.User')),
            ],
            options={
                'db_table': 'user_token',
            },
        ),
        migrations.CreateModel(
            name='ContentTypeExtend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('remark', models.CharField(default=None, max_length=128)),
                ('contenttype', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'db_table': 'content_type_extend',
            },
        ),
    ]
