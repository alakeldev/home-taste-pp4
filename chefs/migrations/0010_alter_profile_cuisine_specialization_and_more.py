# Generated by Django 4.2.9 on 2024-03-04 13:45

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0009_alter_profile_region_alter_profile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cuisine_specialization',
            field=models.CharField(blank=True, help_text='Specify your culinary expertise (e.g., Indian, Syrian, Italian)', max_length=50, null=True, verbose_name='Kitchen Specialization'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, help_text='You can enter a different email from the one used during registration', max_length=50, null=True, verbose_name='Email Contact'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(help_text='You can enter a different name from your username', max_length=30, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True, verbose_name='Phone/Mobile Number'),
        ),
    ]
