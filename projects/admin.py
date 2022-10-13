from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from projects.models import  ProjectImage, Project, ProjectTool

# Register your models here.
#admin.site.register(ProjectModel)
admin.site.register(ProjectImage)
admin.site.register(ProjectTool)

@admin.register(Project)
class ProductAdmin(TranslationAdmin):
    group_fieldsets = True  
    list_display = ("name",)
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }