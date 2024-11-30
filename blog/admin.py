# Importing django modules
from django.urls import reverse
from django.contrib import admin
from django.utils.http import urlencode
from django.utils.html import format_html

# Importing parler module for multilingual support
from parler.admin import TranslatableAdmin

# Importing custom models
from blog.models import Post, Media, Comment, Category

# Importing custom filters
from blog.admin_filters import VerifyFilter, IsDraftFilter

# Importing custom actions
from blog.admin_actions import verify_comment, draft_post, publish_post

# Custom admin for models
class PostAdmin(TranslatableAdmin):
    actions = [draft_post, publish_post]
    list_display = ['published_at', 'is_draft', 'created_by', 'category', 'media', 'updated_at', 'title', 'abstract']
    readonly_fields  = ['author']
    list_filter = [IsDraftFilter, 'category' , 'published_at']
    search_fields = ['title']

    def created_by(self, obj):
        url = (reverse("admin:auth_user_change", args=[obj.author.id]))
        return format_html('<a href="{}"> {}</a>', url, obj.author.username)

    def save_model(self, request, obj, form, change):
        # register author
        if not obj.pk:
            obj.author = request.user
        return super().save_model(request, obj, form, change)

class MediaAdmin(admin.ModelAdmin):
    list_display = ['media_type', 'posts' , 'description']
    search_fields = ['description']
    list_filter = ['media_type']
    def posts(self, obj):
        count = obj.post.count()
        url = (reverse('admin:blog_post_changelist')+
               "?"+
               urlencode({"media__id": f"{obj.id}"}))
        return format_html('<a href="{}">{} related posts</a>', url, count)

class CommentAdmin(TranslatableAdmin):
    actions = [verify_comment]
    list_display = ['full_name', 'post', 'updated_at', 'verify_status']
    list_filter = [VerifyFilter, 'updated_at', 'created_at']
    search_fields = ['first_name']
    
    def full_name(self, obj):
        url = (reverse('admin:blog_comment_change', args=[obj.id]))
        return format_html('<a href="{}">{} {}</a>', url, obj.first_name, obj.last_name)

    def post(self, obj):
        url = (reverse("admin:blog_post_changelist")+
               "?" +
               urlencode({"post__id:": f"{obj.post.id}"}))
        return format_html('<a href="{}">{}</a>',url, obj.post.title)
        
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', "parent", 'post']
    search_fields = ['name']
    list_filter = ['parent']
    
    def post(self, obj):
        count = obj.post.count()
        url = (reverse('admin:blog_post_changelist')+
               "?"+
               urlencode({"category__id": f"{obj.id}"}))
        return format_html('<a href="{}">{} related post</a>',url, count)

admin.site.register(Post, PostAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)