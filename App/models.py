from django.db import models

# Create your models here.
from django.urls import reverse

class Topic(models.Model):
    topic_name=models.CharField(max_length=100)
    index=models.IntegerField()
    locate=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.topic_name
    
    def get_absolute_url(self):
        return reverse('TopicDetail',kwargs={'pk':self.pk})
    
class Webpage(models.Model):
    name=models.CharField(max_length=100)
    url = models.URLField()
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE,related_name='Jelly')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('WebpageDetail',kwargs={'name':self.pk})
    