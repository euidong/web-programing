from django.db import models

# Create your models here.

class User(models.Model) :
    email = models.EmailField(primary_key = True)
    password = models.CharField(max_length = 20)
    first_name = models.CharField(max_length= 10)
    last_name = models.CharField(max_length = 10)
    
    
    class Meta :
        ordering = ('first_name', )
