# Generated by Django 2.2.1 on 2019-05-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='公司名称', max_length=128, null=True, verbose_name='公司名称')),
                ('address', models.CharField(max_length=128, null=True, verbose_name='公司所在国家和城市')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
