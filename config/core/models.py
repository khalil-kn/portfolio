from django.db import models

# Create your models here.
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(blank=True)  # can use URL or later ImageField
    tags = models.CharField(max_length=100, blank=True)  # comma-separated
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def tag_list(self):
        return [tag.strip() for tag in self.tags.split(',') if tag]

    def __str__(self):
        return self.title





