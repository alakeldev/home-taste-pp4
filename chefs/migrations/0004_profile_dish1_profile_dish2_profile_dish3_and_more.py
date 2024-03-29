# Generated by Django 4.2.9 on 2024-02-28 22:09

from django.db import migrations, models
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dish1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[200, None], upload_to='dishes/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dish2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[200, None], upload_to='dishes/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dish3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[200, None], upload_to='dishes/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dish4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[200, None], upload_to='dishes/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tiktok_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Frankfurt, Damascus, Paris...', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(default='Germany, France, Syrian...', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cuisine_specialization',
            field=models.CharField(default='Indian, Syrian, Italian...', max_length=150),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male')], null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[400, None], upload_to='profile/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instructions',
            field=djrichtextfield.models.RichTextField(default='Please Enter Your Instructions/Schedules/Notes...', max_length=20000),
        ),
    ]
