# Generated by Django 3.0.3 on 2020-08-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_auto_20200813_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='listing_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),

    ]
