# blog/admin.py
from django.contrib import admin
from .models import Post
from .models import Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'content_size', 'created_at', 'author']
    list_display_links = ['id', 'title', 'created_at', 'author']
    list_per_page = 5
    actions = ['make_published', 'make_draft']

    def content_size(self, post):
        return '{}글자'.format(len(post.content))

    content_size.short_description = "내용 글자수"

    def make_published(self, request, queryset):
        updated_count = queryset.update(status='p')
        self.message_user(request, '{}건의 포스팅을 published 상태로 변경'.format(updated_count))

    make_published.short_description = " 지정 포스팅을 published 상태로 변경합니다."

    def make_draft(self, request, queryset):
        updated_count = queryset.update(status='d')
        self.message_user(request, '{}건의 포스팅을 draft 상태로 변경'.format(updated_count))

    make_draft.short_description = " 지정 포스팅을 draft 상태로 변경합니다."


# admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    pass
