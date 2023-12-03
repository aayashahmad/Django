from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    desc = models.TextField()
    
    def __str__(self):
        return self.name + " : " + self.email