# Generated by Django 3.2.6 on 2021-12-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_fav'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='ownerInfo',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='listing',
            name='ownerName',
            field=models.CharField(default='Unknown', max_length=200),
        ),
        migrations.AddField(
            model_name='listing',
            name='ownerPh',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]