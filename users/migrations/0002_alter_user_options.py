# Generated by Django 4.2.1 on 2023-07-11 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('email',), 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
