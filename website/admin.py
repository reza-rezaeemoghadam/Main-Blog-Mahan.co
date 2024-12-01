# Importing django modules
from django.urls import reverse
from django.contrib import admin
from django.utils.http import urlencode
from django.utils.html import format_html

# Importing parler modules
from parler.admin import TranslatableAdmin

# Importing custom models
from website.models import Section, Part, ContactUs, VisitUs, SocialLinks
# Implementing custom admin models
class SectionAdmin(TranslatableAdmin):
    list_display = ['title', 'content', 'parts', 'updated_at', 'number'] 
    list_filter = ['updated_at']   

    def content(self, obj):
        return obj.content[:20]
    
    def parts(self, obj):
        count = obj.parts.count()
        url = (reverse('admin:website_part_changelist')+
               "?"+
               urlencode({'section__id': f"{obj.id}"}))
        return format_html('<a href="{}">{} related parts</a>', url, count)
    
class PartAdmin(TranslatableAdmin):
    list_display = ['title', 'sub_title', 'updated_at', 'sections', 'number']
    search_fields = ['title', 'sub_title']
    list_filter = ['section']
    def sections(self, obj):
        url = (reverse('admin:website_section_change',args=[obj.section.id]))
        return format_html('<a href="{}">{} </a>', url, obj.section.title)

class ContactUsAdmin(TranslatableAdmin):
    list_display = ['full_name', 'email', 'updated_at', 'sections']
    list_filter = ['updated_at', 'section']
    search_fields = ['name', 'email']
    
    def sections(self, obj):
        url = (reverse('admin:website_section_change',args=[obj.section.id]))
        return format_html('<a href="{}">{}</a>', url, obj.section.title)

    def full_name(self, obj):
        url = reverse('admin:website_contactus_change', args=[obj.id])
        return format_html('<a href="{}">{}</a>', url, obj.name)


class VisitUsAdmin(TranslatableAdmin):
    list_display = ['address', 'email', 'updated_at', 'sections']

    def sections(self, obj):
        url = (reverse('admin:website_section_change',args=[obj.section.id]))
        return format_html('<a href="{}">{} </a>', url, obj.section.title)


class SocialLinksAdmin(TranslatableAdmin):
    list_display = ['name', 'updated_at', 'sections']
    list_filter = ['updated_at', 'section']
    search_fields = ['name']

    def sections(self, obj):
        url = (reverse('admin:website_section_change',args=[obj.section.id]))
        return format_html('<a href="{}">{} </a>', url, obj.section.title)


admin.site.register(Section, SectionAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(VisitUs, VisitUsAdmin)
admin.site.register(SocialLinks, SocialLinksAdmin)