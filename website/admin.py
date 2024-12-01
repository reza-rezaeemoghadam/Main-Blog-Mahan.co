# Importing django modules
from django.contrib import admin

# Importing parler modules
from parler.admin import TranslatableAdmin

# Importing custom models
from website.models import Section, Part, ContactUs, VisitUs, SocialLinks
# Implementing custom admin models
class SectionAdmin(TranslatableAdmin):
    pass

class PartAdmin(TranslatableAdmin):
    pass

class ContactUsAdmin(TranslatableAdmin):
    pass

class VisitUsAdmin(TranslatableAdmin):
    pass

class SocialLinksAdmin(TranslatableAdmin):
    pass

admin.site.register(Section,TranslatableAdmin)
admin.site.register(Part,TranslatableAdmin)
admin.site.register(ContactUs,TranslatableAdmin)
admin.site.register(VisitUs,TranslatableAdmin)
admin.site.register(SocialLinks,TranslatableAdmin)