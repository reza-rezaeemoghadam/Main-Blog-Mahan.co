# Importing django modules
from django.contrib import admin

# Importing parler module for multilingual support
from parler.admin import TranslatableAdmin

# Importing custom models
from blog.models import Post, Media, Comment, Category

class PostAdmin(TranslatableAdmin):
    list_display = ['published_at', 'is_draft', 'author', 'category', 'media', 'updated_at', 'title', 'abstract', 'body']
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

admin.site.register(Post, PostAdmin)
admin.site.register(Media)
admin.site.register(Comment, TranslatableAdmin)
admin.site.register(Category, TranslatableAdmin)
