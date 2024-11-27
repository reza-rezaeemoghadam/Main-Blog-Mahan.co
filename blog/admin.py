# Importing django modules
from django.urls import reverse
from django.contrib import admin
from django.utils.http import urlencode
from django.utils.html import format_html

# Importing parler module for multilingual support
from parler.admin import TranslatableAdmin

# Importing custom models
from blog.models import Post, Media, Comment, Category

class PostAdmin(TranslatableAdmin):
    list_display = ['published_at', 'is_draft', 'author', 'category', 'media', 'updated_at', 'title', 'abstract']
    readonly_fields  = ['author']

    def save_model(self, request, obj, form, change):
        # Check draft and published status
        if obj.is_published:
            obj.is_draft = False
        if not obj.is_draft and not obj.is_published:
            obj.is_draft = True
        # register author
        if not obj.pk:
            obj.author = request.user
        return super().save_model(request, obj, form, change)

class MediaAdmin(admin.ModelAdmin):
    list_display = ['media_type', 'posts' , 'description']
    def posts(self, obj):
        count = obj.post_set.count()
        url = (reverse('admin:blog_post_changelist')+
               "?"+
               urlencode({"media__id": f"{obj.id}"}))
        return format_html('<a href="{}">{} related posts</a>', url, count)

class CommentAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Comment, TranslatableAdmin)
admin.site.register(Category, TranslatableAdmin)
