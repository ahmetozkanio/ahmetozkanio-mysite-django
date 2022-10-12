from django.contrib import admin

from certificates.models import CertificatesModel

# Register your models here.
admin.site.register(CertificatesModel)
class CertificatesAdmin(admin.ModelAdmin):
    list_display = ('name','company_name','date','avaliable')