from django.db import models

# Create your models here.
class web_users(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    theme_c1 = models.CharField(max_length=128,default="")
    theme_c2 = models.CharField(max_length=128,default="")
    theme_c3 = models.CharField(max_length=128,default="")
    theme_c4 = models.CharField(max_length=128,default="")

    def __str__(self):
        return self.email

class note(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    email = models.CharField(max_length=128)

    def __str__(self):
        return self.title
    
    
    
