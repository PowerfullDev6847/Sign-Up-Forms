from django.db import models

class WebUser(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=20) 
    show = models.BooleanField()
    create= models.DateTimeField(auto_now_add=True)
    update= models.DateTimeField(auto_now=True)
