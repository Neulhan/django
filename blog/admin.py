# blog/admin.py
from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'created_at', 'author']
    list_display_links = ['id', 'title', 'created_at', 'author']
    list_per_page = 5

    def content_size(self, post):
        return '{}글자'.format(len(post.content))
    content_size.short_description = "내용 글자수"
# admin.site.register(Post, PostAdmin)
