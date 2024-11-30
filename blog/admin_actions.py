# Importing django modules
from django.contrib import admin

# Custom action
@admin.action(description="Publishing selected posts")
def publish_post(modeladmin, request, queryset):
    return queryset.update(is_published=True, is_draft=False)

@admin.action(description="Drafting selected posts")
def draft_post(modeladmin, request, queryset):
    return queryset.update(is_draft=True, is_published=False)

@admin.action(description="Verfying selected comments")
def verify_comment(modeladmin, request, queryset):
    return queryset.update(verify_status=True)