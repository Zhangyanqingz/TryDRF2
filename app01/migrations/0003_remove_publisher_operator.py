# Generated by Django 2.0 on 2019-05-24 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20190222_0730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='operator',
        ),
    ]
