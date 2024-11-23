# Importing django modules
from django.contrib import admin

# Importing parler module for multilingual support
from parler.admin import TranslatableAdmin

# Importing custom models
from blog.models import Post, Media, Comment

admin.site.register(Post, TranslatableAdmin)
admin.site.register(Media)
admin.site.register(Comment, TranslatableAdmin)
