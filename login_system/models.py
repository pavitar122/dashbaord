from django.db import models



# Create your models here.

class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='static/images/Doctor/')
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='static/images/Patient/')
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='static/images/blog_images/')
    category = models.CharField(max_length=100)
    summary = models.TextField()
    content = models.TextField()
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'