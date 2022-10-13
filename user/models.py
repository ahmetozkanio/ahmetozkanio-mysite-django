from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class UserModel(models.Model):

    user_name = models.CharField(max_length = 64)
    firs_name = models.CharField(max_length = 64)
    last_name = models.CharField(max_length = 64)
    title = models.CharField(max_length = 128)
    email = models.EmailField()
    image  =  models.ImageField(upload_to="user")
    description = RichTextField()
    birthday = models.DateTimeField(auto_now=True)
    avaliable = models.BooleanField(default =True)

    def __str__(self):
        return self.firs_name

class UserImage(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_images')
    image = models.ImageField(upload_to= "user/images")
    def __str__(self):
        return self.user

class Account(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='user_accounts')
    account_name = models.CharField(max_length = 64, unique = True)
    account_image = models.FileField(upload_to = "account")
    account_url = models.URLField(blank=True,null=True)
    def __str__(self):
        return self.account_name