# Generated by Django 3.0.3 on 2020-08-13 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auto_20200812_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='starting',
            field=models.BooleanField(),
        ),
        migrations.CreateModel(
            name='SingleWatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(null=True)),
                ('watchlist_item', models.ManyToManyField(blank=True, related_name='watchlist_item', to='auctions.AuctionListing')),
                ('watchlist_u', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
