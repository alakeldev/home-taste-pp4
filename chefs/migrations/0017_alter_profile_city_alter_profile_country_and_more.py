# Generated by Django 4.2.9 on 2024-03-10 00:11

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('chefs', '0016_alter_profile_city_alter_profile_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, help_text='Please enter your city of residence (use abbreviations if its long).', max_length=12, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, help_text='Please enter your country of residence (use abbreviations if its long).', max_length=12, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cuisine_specialization',
            field=models.CharField(blank=True, help_text='Please specify one or two cuisines from your culinary expertise (e.g., Indian, Syrian, Italian)', max_length=25, null=True, verbose_name='Cuisine Type'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, help_text='You can enter a different email from the one used during registration.', max_length=50, null=True, verbose_name='Contact Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instructions',
            field=djrichtextfield.models.RichTextField(blank=True, max_length=6000, null=True, verbose_name='Please Share Below Your Cook Instructions/Schedules'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Please provide your contact phone/mobile number.', max_length=25, null=True, verbose_name='Phone Number'),
        ),
    ]
