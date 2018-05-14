# Generated by Django 2.0.4 on 2018-05-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.IntegerField()),
                ('room', models.IntegerField()),
                ('coins', models.IntegerField()),
                ('rent_buy', models.IntegerField()),
                ('dayq_rent', models.IntegerField()),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
    ]
