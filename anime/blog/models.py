from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    image = models.ImageField(upload_to='posts_img')
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'