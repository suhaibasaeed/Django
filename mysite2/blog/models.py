from django.db import models

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

    def __str__(self):
        """ Return string representation of object"""
        return self.title
    