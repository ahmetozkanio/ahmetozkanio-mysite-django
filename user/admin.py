from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from user.models import Account, UserImage, UserModel

# Register your models here.
# admin.site.register(Account)
# admin.site.register(UserImage)


class UserAccountAdmin(admin.StackedInline):
    model = Account 
class UserImageAdmin(admin.StackedInline):
    model = UserImage 

@admin.register(UserModel)
class ProductAdmin(TranslationAdmin):
    group_fieldsets = True  
    inlines = [UserAccountAdmin,UserImageAdmin]
    list_display = ("title",)
    
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }