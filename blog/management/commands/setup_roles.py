# Importing django modules
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import Post

class Command(BaseCommand):
    help = "Setting up the role permissions"
    def handle(self, *args, **options):
        author_group, created = Group.objects.get_or_create(name="Author")

        content_type = ContentType.objects.get_for_model(Post)
        post_permission = Permission.objects.filter(content_type=content_type)

        for perm in post_permission:
            print(perm)
            author_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Successfully set up group permissions'))
