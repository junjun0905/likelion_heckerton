# Generated by Django 2.2.4 on 2019-08-09 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_num', models.IntegerField()),
                ('phonenum', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='store',
            name='num',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='store',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
