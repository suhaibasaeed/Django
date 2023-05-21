from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    # Auto populate slug field with title field
    prepopulated_fields = {'slug': ('title',)}
    # Filter by author field
    raw_id_fields = ('author',)
    # Navigation links to navigate through date hierarchy
    date_hierarchy = 'publish'