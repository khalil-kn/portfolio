from django.db import models

# Create your models here.
from django.db import models



# Tags as a model by itself is better for scalabilty 
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)    
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title





