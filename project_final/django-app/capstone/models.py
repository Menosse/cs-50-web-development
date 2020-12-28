from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    pass
    def serialize(self):
        return{
            "id": self.id,
            "user": self.username,
            "email": self.email,
        }

class Intro(models.Model):
    intro_description = models.TextField(blank=True)
    #intro_timestamp = models.DateTimeField(auto_now=True)
    intro_pic = models.ImageField(null=True, blank=True, upload_to='intro/')

    def serialize(self):
        return {
            "id": self.id,
            "description": self.intro_description,
            #"timestamp": self.intro_timestamp.strftime("%b %#d %Y, %#I:%M %p"),
            "intro_pic": self.intro_pic.url,
        }

class Bio(models.Model):
    bio_description = models.TextField(blank=True)
    bio_resume = models.TextField(blank=True)
    bio_pic = models.ImageField(null=True, blank=True, upload_to='bio/')

    def serialize(self):
        return {
            "id": self.id,
            "description": self.bio_description,
            "resume": self.bio_resume,
            "bio_pic": self.bio_pic.url,
        }

class Project(models.Model):
    name = models.TextField(blank=True)
    project_description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='project/')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.project_description,
            "main_image": self.image.url
        }
    def __str__(self):
        return self.project_description

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'images/')
    
    def serialize(self):
        return{
            "id": self.id,
            "images": self.images.url
        }

    def __str__(self):
        return self.project.project_description

class Contact(models.Model):
    contact_email = models.TextField(blank=True)
    contact_phone = models.TextField(blank=True)
    contact_address = models.TextField(blank=True)
    contact_instagram = models.TextField(blank=True)
    contact_twitch = models.TextField(blank=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.contact_email,
            "phone": self.contact_phone,
            "address": self.contact_address,
            "instagram": self.contact_instagram,
            "twitch": self.contact_twitch,
        }