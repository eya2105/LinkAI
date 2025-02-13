from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to="profile_pics", null=True, default="default.jpg")
    bio=models.TextField(blank=True)
    location=models.CharField(max_length=100,blank=True)
    skills=models.TextField(blank=True)#seperated by a comma
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)  # GitHub profile link
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)  # Resume file

    def __str__(self):
        return f"{self.user.username} Profile"
    