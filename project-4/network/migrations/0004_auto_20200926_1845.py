# Generated by Django 3.0.3 on 2020-09-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_post_liked_by_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
