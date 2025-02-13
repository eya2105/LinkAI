from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to="profile_pics", null=True, default="default.jpg")
    bio=models.TextField(blank=True)
    location=models.CharField(max_length=100,blank=True)
    skills=models.TextField(blank=True)#seperated by a comma
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)  # GitHub profile link
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)  # Resume file

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.user.username} Profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
def create_user_profile(sender, instance, created, **kwargs):
	if created:
	    Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()    
 
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)