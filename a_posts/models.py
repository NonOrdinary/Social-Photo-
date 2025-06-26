from django.db import models
import uuid
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=500)  # there does exist TextField with unlimited length
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    #special function to set name of the instance of the object as title
    def __str__(self):
        return str(self.title)
    