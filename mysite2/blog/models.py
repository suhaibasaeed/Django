from django.db import models
from django.utils import timezone

# Create your models here.
# Data model for blog posts
class Post(models.Model):
    """ Posts have title, short label (slug) and body"""
    
    # Charfield corresponds to VARCHAR column in SQL DB
    title = models.CharField(max_length=250)
    # Also a VARCHAR column, but used to build a URL
    slug = models.SlugField(max_length=250)
    # Textfield corresponds to TEXT column in SQL DB - 
    body = models.TextField()
    # Date and time of publication - DATETIME column in SQL DB
    publish = models.DateTimeField(default=timezone.now)
    # Store when object was created
    created = models.DateTimeField(auto_now_add=True)
    # Store when object was last updated - auto update date when object is saved
    updated = models.DateTimeField(auto_now=True)

    # Meta class to specify model-specific options
    class Meta:
        # Order results by publish field in descending order
        ordering = ('-publish',)
    
    def __str__(self):
        """ Return string representation of object"""
        return self.title
    
    