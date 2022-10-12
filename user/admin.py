from django.contrib import admin

from user.models import Accounts, UserModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(Accounts)
