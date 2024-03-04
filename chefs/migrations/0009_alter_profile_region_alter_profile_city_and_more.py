# Generated by Django 4.2.9 on 2024-03-04 13:08

from django.db import migrations, models
import django_resized.forms
import djrichtextfield.models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0008_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Region',
            field=models.CharField(choices=[('Africa', 'Africa'), ('Asia', 'Asia'), ('Caribbean', 'Caribbean'), ('Central America', 'Central America'), ('Europe', 'Europe'), ('North America', 'North America'), ('Oceania', 'Oceania'), ('South America', 'South America')], default='Europe', verbose_name='Please Choose Your Current Region'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Current City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Current Country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cuisine_specialization',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Kitchen Specialization'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dish1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/', verbose_name="Dish's Image One"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dish2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/', verbose_name="Dish's Image Two"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dish3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/', verbose_name="Dish's Image Three"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dish4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/', verbose_name="Dish's Image Four"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dish5',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[600, 600], upload_to='dishes/', verbose_name="Dish's Image Five"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email Contact'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_link',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook Profile Link'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[400, None], upload_to='profile/', verbose_name='Profile Picture'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_link',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram Profile Link'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instructions',
            field=djrichtextfield.models.RichTextField(blank=True, max_length=20000, null=True, verbose_name='Please Share Below Your Instructions/Cook Schedules'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='Mobile Number'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tiktok_link',
            field=models.URLField(blank=True, null=True, verbose_name='Tiktok Profile Link'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='youtube_link',
            field=models.URLField(blank=True, null=True, verbose_name='Youtube Channel Link'),
        ),
    ]
