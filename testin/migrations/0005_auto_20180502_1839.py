# Generated by Django 2.0.4 on 2018-05-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testin', '0004_auto_20180502_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='day_rent',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='rent_buy',
            field=models.BooleanField(),
        ),
    ]
