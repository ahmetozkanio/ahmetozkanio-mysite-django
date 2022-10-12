from django.contrib import admin

from user.models import AccountModel, UserImagesModel, UserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(AccountModel)
admin.site.register(UserImagesModel)