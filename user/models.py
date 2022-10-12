from django.db import models


# Create your models here.
class UserModel(models.Model):
    firs_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    title = models.CharField(max_length = 128)
    image  = models.ImageField(upload_to="user")
    description = models.TextField(blank=True)
    birthday = models.DateTimeField(auto_now=True)
    avaliable = models.BooleanField(default =True)

    def __str__(self):
        return self.firs_name

class Accounts(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_accounts')
    account_name = models.CharField(max_length = 64, unique = True)
    account_image = models.ImageField(upload_to="account")
    account_url = models.URLField(blank=True,null=True)