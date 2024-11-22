from django.contrib import admin
from blog.models import Post

# Importing custom models
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    ordering = ('created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.has_perm('blog.can_manage_posts'):
            return qs.filter(author=request.user)
        return qs

    def has_change_permission(self, request, obj=None):
        if obj and request.user.has_perm('blog.can_manage_posts'):
            return obj.author == request.user
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if obj and request.user.has_perm('blog.can_manage_posts'):
            return obj.author == request.user
        return super().has_delete_permission(request, obj)

admin.site.register(Post, PostAdmin)