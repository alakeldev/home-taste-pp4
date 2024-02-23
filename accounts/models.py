from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.

GENDER = (("F", "Female"), ("M", "Male"))

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    cuisine_specialization = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=25, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile', blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    twitter_account = models.CharField(max_length= 80, blank=True, null=True)
    youtube_account = models.CharField(max_length= 80, blank=True, null=True)
    facebook_account = models.CharField(max_length= 80, blank=True, null=True)
    instagram_account = models.CharField(max_length= 80, blank=True, null=True)
    gender = models.CharField(choices = GENDER, blank=True, null=True)


    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f"User: {self.user} | Name: {self.name}"
    



def create_profile(sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)