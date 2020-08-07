# Generated by Django 3.0.3 on 2020-08-07 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20200807_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='auctionlisting_user',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, related_name='auctionlisting_user', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='description',
            field=models.CharField(default=3, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='starting_bid',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='title',
            field=models.CharField(default=4, max_length=64),
            preserve_default=False,
        ),
    ]