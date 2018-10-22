from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile/')
    bio = models.CharField(max_length=500, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    hood = models.ForeignKey('Hood', blank = True, null=True)
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(request, user_id):
        user = User.objects.get(pk=user_id)
        user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'    
        user.save

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']


class Hood(models.Model):
    hood_name = models.CharField(max_length=25)
    hood_image = models.ImageField(upload_to='hood/', null=True)
    AREA_CHOICES = (
        ('Westlands', 'Westlands Constituency'),
        ('Dagoretti', 'Dagoretti Constituency'),
        ('Langata', 'Langata Constituency'),
        ('Kasarani', 'Kasarani Constituency'),
        ('Embakasi', 'Embakasi Constituency'),
        ('Starehe', 'Starehe Constituency'),
        ('Kamkunji', 'Kamkunji Constituency'),
    )
    hood_location = models.CharField(max_length = 25, choices = AREA_CHOICES)
    hood_count = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def find_hood(cls, hood_id):
        hood = cls.objects.filter(title__icontains=search_term)
        return hood

    def __str__(self):
        return self.hood_name

    class Meta:
        ordering = ('hood_name',)


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='business/')
    business_email = models.EmailField()

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_by_business_name(cls, search_term):
        hood = cls.objects.filter(business_name__icontains=search_term)
        return hood

    def update_business(self):
        self.update()

    def __str__(self):
        return self.business_name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=250)
    hood = models.ForeignKey(Hood, blank=True, on_delete=models.CASCADE)
