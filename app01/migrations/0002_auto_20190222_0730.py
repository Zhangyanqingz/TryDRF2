# Generated by Django 2.0.5 on 2019-02-22 07:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='书名')),
            ],
            options={
                'verbose_name': '书',
                'verbose_name_plural': '书',
            },
        ),
        migrations.AlterField(
            model_name='publisher',
            name='operator',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL, verbose_name='操作人'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete='CASCADE', to='app01.Publisher'),
        ),
    ]
