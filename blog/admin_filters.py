# Importing django moudles
from django.contrib.admin import SimpleListFilter

# Custom filters
class VerifyFilter(SimpleListFilter):
    title = "Verified"
    parameter_name = "verified"

    def lookups(self, request, model_admin):
        return [('verified', 'Verified'), ("not verified", "Not verified")]
    
    def queryset(self, request, queryset):
        if self.value() == "verified":
            return queryset.filter(verify_status=True)            
        elif self.value() == "not verified":
            return queryset.filter(verify_status=False)            
        else:
            return queryset
        
class IsDraftFilter(SimpleListFilter):
    title = "Draft"
    parameter_name = "is_draft"

    def lookups(self, request, model_admin):
        return  [('true', 'True'), ("false", "False")]

    def queryset(self, request, queryset):
        if self.value() == "true":
            return queryset.filter(is_draft=True)
        elif self.value() == 'false':             
            return queryset.filter(is_draft=False)            
        else:            
            return queryset            