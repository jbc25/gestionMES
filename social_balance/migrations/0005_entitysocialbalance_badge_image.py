# Generated by Django 2.1.12 on 2019-10-17 13:11

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('social_balance', '0004_socialbalancebadge_base_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='entitysocialbalance',
            name='badge_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='balances', verbose_name='Imagen del sello'),
        ),
    ]
