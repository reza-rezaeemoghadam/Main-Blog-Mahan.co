# Importing django modules
from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Importing parler modules
from parler.models import TranslatableModel, TranslatedFields

# Importing text editor
from django_ckeditor_5.fields import CKEditor5Field

 # Importing needed Const from settings
from src.settings import MEDIA_ROOT

# Importing custom models

# Create models
class Media(models.Model): 
    MEDIA_TYPES = [ ('image', 'Image'), 
                   ('video', 'Video'), 
                   ('document', 'Document'), ] 
    file = models.FileField(upload_to='media/') 
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES) 
    description = models.TextField(blank=True, verbose_name=_("Description")) 

    def __str__(self): 
        return self.file.name

# TODO: Implementing Tags is the second priority
# class Tag(TranslatableModel):
#     pass

class Category(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=50 , unique=True, verbose_name=_('category|name')),
        description = models.TextField(blank=True, verbose_name=_('category|description'))
    )
    
    parent = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('category|subcategory'))
    created_at = models.DateTimeField(editable=False, blank=True)
    updated_at = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Category, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Post(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=100, verbose_name=_('post|title'), unique=True),
        abstract = models.CharField(max_length=200,  verbose_name=_('post|abstract')),
        body = CKEditor5Field(config_name='default', verbose_name=_('post|body'))
    )
    #TODO: later try to implement image field with Base64 encoding
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name=_('post|is_published'))
    is_draft = models.BooleanField(default=False, verbose_name=_('post|is_draft'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('post|created_by'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('post|category'), related_name="post")
    media = models.ForeignKey(Media , on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_('post|media'), related_name="post")

    created_at = models.DateTimeField(editable=False, blank=True)
    updated_at = models.DateTimeField(blank=True)

    def publish(self): 
        self.published_at = timezone.now() 
        self.is_published = True 
        self.is_draft = False 
        self.save()

    def save(self, *args, **kwargs):
        # Handling is_published and is_draft
        if self.is_published:
            self.is_draft = False
        if not self.is_draft and not self.is_published:
            self.is_draft = True
        # Handling author registration
        if not self.id and 'request' in kwargs: 
            self.author = kwargs.pop('request').user        
        # Handling created_at and updated_at 
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

class Comment(TranslatableModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name=_('comment|post'))
    first_name = models.CharField(max_length=20, verbose_name=_('comment|first_name'))
    last_name = models.CharField(max_length=30, verbose_name=_('comment|last_name'))
    phone = models.CharField(max_length=16, verbose_name=_('comment|phone'))
    verify_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(editable=False, blank=True)
    updated_at = models.DateTimeField(blank=True)
    translations = TranslatedFields(content = models.TextField(verbose_name=_('comment|content')))

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return f'Comment by {self.first_name} {self.last_name} on {self.post}'
    
    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')