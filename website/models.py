# Importing django modules
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Importing extra modules

# Importing praler modules
from parler.models import TranslatableModel, TranslatedFields

# Implementing custom models
class Section(TranslatableModel):
    translation = TranslatedFields(
        title = models.CharField(max_length=100, verbose_name=_("section|title")),
        content = models.TextField(verbose_name=_("section|content")),
    )
    number = models.SmallIntegerField(verbose_name=_("section|number"))
    created_at = models.DateTimeField(editable=False, blank=True)
    updated_at = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Section, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')

class Part(TranslatableModel):
    translation = TranslatedFields(
                  title = models.CharField(max_length=60, verbose_name=_("part|title")),
                  sub_title = models.CharField(max_length=50, verbose_name=_("part|sub_title")),
                  content = models.TextField(verbose_name=_("part|content")),
    )
    image = models.ImageField(upload_to="media/landing/", verbose_name=_("part|image"))
    number = models.SmallIntegerField(verbose_name=_('part|number'))   
    url = models.URLField(verbose_name=_("part|url"))
    section  = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="parts", verbose_name=_("part|section"))
    created_at = models.DateTimeField(editable=False, blank=True)
    updated_at = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Part, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = _('Part')
        verbose_name_plural = _('Parts')

class ContactUs(TranslatableModel):
    translation = TranslatedFields(
        name = models.CharField(max_length=50, verbose_name=_("contactus|name")),
        email =models.EmailField(verbose_name=_("contactus|email")),
        phone = models.CharField(max_length=20, verbose_name=_("contactus|phone")),
        content = models.TextField(verbose_name=_("contactus|content")),
    )
    website = models.URLField(verbose_name=_("contactus|website")),
    section = models.OneToOneField(Section, on_delete=models.CASCADE, related_name="contact_us", verbose_name=_("contactus|section"))
    created_at = models.DateTimeField(editable=False, blank=True)
    updated_at = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(ContactUs, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}-{self.email}"

    class Meta:
        verbose_name = _("Contact Us")
        verbose_name_plural = _("Contact Us")

class VisitUs(TranslatableModel):
    translation = TranslatedFields(
        address = models.CharField(max_length=255, verbose_name=_("visitus|address")),
        phone = models.CharField(max_length=16, verbose_name=_("visius|phone")),
        email = models.EmailField(verbose_name=_("visitus|email")),        
    )
    section = models.OneToOneField(Section, on_delete=models.CASCADE, related_name="visit_us", verbose_name=_("visitus|section"))
    created_at = models.DateTimeField(editable=False, blank=True)
    updated_at = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(VisitUs, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Visit Us")
        verbose_name_plural = _("Visit Us")

class SocialLinks(TranslatableModel):
    translation = TranslatedFields(
        name = models.CharField(max_length=50, unique=True, verbose_name=_("social|name")),
    )
    icon = models.ImageField(upload_to="media/icons/")
    url = models.URLField(verbose_name="social|url")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="social_links", verbose_name=_("social|section"))
    created_at = models.DateTimeField(editable=False, blank=True)
    updated_at = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(SocialLinks, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Social Link")
        verbose_name_plural = _("Social Links")