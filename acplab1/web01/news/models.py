from django.db import models

# Create your models here.
class NewsPost(models.Model):
    posttitle = models.CharField(max_length=200)
    newscontent = models.TextField()
    def __str__(self):
        return self.title
