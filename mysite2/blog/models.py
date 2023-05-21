from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Data model for blog posts
class Post(models.Model):
    """ Posts have title, short label (slug) and body"""
    
    # Status field of posts - Enum class
    class Status(models.TextChoices):
        # Available choices
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    
    # Charfield corresponds to VARCHAR column in SQL DB
    title = models.CharField(max_length=250)
    # Also a VARCHAR column, but used to build a URL
    slug = models.SlugField(max_length=250)
    # Foreign key to User model - One to many relationship
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # Textfield corresponds to TEXT column in SQL DB - 
    body = models.TextField()
    # Date and time of publication - DATETIME column in SQL DB
    publish = models.DateTimeField(default=timezone.now)
    # Store when object was created
    created = models.DateTimeField(auto_now_add=True)
    # Store when object was last updated - auto update date when object is saved
    updated = models.DateTimeField(auto_now=True)
    # Status of post - Enum class
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)


    # Meta class to specify metadata about the model
    class Meta:
        # Order results by publish field in descending order - Used for DB queries
        ordering = ('-publish',)
        # DB index for publish field - Improve performance of queries
        indexes = [
            models.Index(fields=['-publish',]),
        ]
    
    def __str__(self):
        """ Return string representation of object"""
        return self.title
    
    