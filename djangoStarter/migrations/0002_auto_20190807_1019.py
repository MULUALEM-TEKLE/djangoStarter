# Generated by Django 2.2 on 2019-08-07 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoStarter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date']},
        ),
    ]
