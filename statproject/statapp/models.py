from django.db import models

# Create your models here.
class products(models.Model):
    name=models.TextField(max_length=300)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

def __str__(self):
    return self.name