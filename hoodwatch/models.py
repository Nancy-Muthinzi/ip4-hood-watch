from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile', default=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile/', default=True)
    bio = models.CharField(max_length=200, default=True)
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
    hood_location = models.CharField(max_length=50)
    occupants_count = models.IntegerField()   
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE, null=True)

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()    

    @classmethod
    def find_hood(cls,hood_id):
        hood = cls.objects.filter(title__icontains=search_term)
        return hood

    def update_hood(self):
        self.update()

    def update_occupants(self):
        self.update()        