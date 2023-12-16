from django.db import models

# Create your models here.
class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add='True')

    first_name = models.CharField(max_length=100)
    
    last_name = models.CharField(max_length=100)
    
    nick_name = models.CharField(max_length=30)
    
    phone = models.CharField(max_length=20, blank=True)
    
    twitter = models.CharField(max_length=50, blank=True)
    
    snapchat = models.CharField(max_length=50, blank=True)
    
    email = models.EmailField(blank=True)
    
    address = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.nick_name
