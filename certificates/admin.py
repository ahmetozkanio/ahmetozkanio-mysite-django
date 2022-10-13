from django.contrib import admin

from certificates.models import Certificate

# Register your models here.
admin.site.register(Certificate)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ('name','company_name','date','avaliable')