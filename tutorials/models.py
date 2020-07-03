from django.db import models

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

class Student(models.Model):
    name = models.CharField(max_length=255, blank=False, default='')
    nim = models.CharField(max_length=255, blank=False, default='')
    generation = models.IntegerField(blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    avatar = models.ImageField(blank=True, default='')
    major = models.CharField(max_length=255, blank=False, default='')
    address = models.CharField(max_length=255, blank=False, default='')
    city = models.CharField(max_length=255, blank=False, default='')
    province = models.CharField(max_length=255, blank=False, default='')
    postal_code = models.IntegerField(blank=False, default='')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
