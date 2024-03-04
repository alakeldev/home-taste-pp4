# Generated by Django 4.2.9 on 2024-03-04 08:20

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0006_profile_dish5_profile_email_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dish1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dish2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dish3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dish4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dish5',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]