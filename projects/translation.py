
from modeltranslation.translator import  TranslationOptions,register
from .models import Project

@register(Project)
class UserTranslationOptions(TranslationOptions):
    fields = ('name', 'description','slug')
