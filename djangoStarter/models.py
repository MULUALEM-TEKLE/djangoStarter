from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    
    image = models.FileField(upload_to='images/')
    title = models.CharField(default="" , max_length=64)
    description = models.CharField(default="" , max_length=512)
    date = models.DateField(default=datetime.date.today)

    class meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.title