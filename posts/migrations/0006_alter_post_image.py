# Generated by Django 3.2.23 on 2024-02-22 07:33

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20240214_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='../default_post_uxb6vu', upload_to='images/'),
        ),
    ]
