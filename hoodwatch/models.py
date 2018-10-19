from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField

class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', default=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile/', default=True)
    bio = models.CharField(max_length=500)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)
    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        ordering = ['first_name', 'last_name']

class Hood(models.Model):
    hood_name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    hood_location = PlainLocationField(based_fields=['city'], zoom=7)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()    

    @classmethod
    def find_hood(cls,hood_id):
        hood = cls.objects.filter(title__icontains=search_term)
        return hood

    def __str__(self):
        return self.hood_name 

    class Meta:
        ordering = ('hood_name',) 

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, default=True, on_delete=models.CASCADE)
    hood_id = models.ForeignKey(Hood, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='business/', default=True)
    business_email = models.EmailField()

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()    

    @classmethod
    def search_by_business_name(cls,search_term):
        hood = cls.objects.filter(business_name__icontains=search_term)
        return hood

    def update_business(self):
        self.update()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length=500)
    hood = models.ForeignKey(Hood, blank=True,on_delete=models.CASCADE)
