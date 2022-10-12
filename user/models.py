from django.db import models


# Create your models here.
class UserModel(models.Model):
    
    firs_name = models.CharField()
    last_name = models.CharField()
    title =  models.CharField()
    image  = models.ImageField(upload_to="user")
    description = models.TextField(blank=True)
    birthday = models.DateTimeField(auto_now=True)
    accounts = models.CharField()
    avaliable = models.BooleanField(default =True)

    def __str__(self):
        return self.firs_name

class Accounts(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_accounts')
    account_name = models.CharField()
    account_image = models.ImageField(upload_to="account")
    account_url = models.URLField(blank=True,null=True)