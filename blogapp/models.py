from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=264)
    text = models.TextField(default='')
    published_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.published_date = timezone.now()
        super().save(*args,**kwargs) 
    
    def get_absolute_url(self):
        return reverse('blogapp:post_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ["-published_date"]


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.CharField(max_length=264)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.text

    
    




