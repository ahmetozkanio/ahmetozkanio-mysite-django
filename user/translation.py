
from modeltranslation.translator import  TranslationOptions,register
from .models import UserModel

@register(UserModel)
class UserTranslationOptions(TranslationOptions):
    fields = ('description', 'title')
