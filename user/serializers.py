

from .models import AccountModel, UserImagesModel, UserModel

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImagesModel
        fields = '__all__'
class UserAccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = '__all__'

class UserModelSerializer(ModelSerializer):
    user_images = UserImagesSerializer(many=True, read_only=True)
    user_accounts = UserAccountsSerializer(many=True, read_only=True)
    class Meta:
        model = UserModel
        fields = ('id','user_name', 'firs_name','last_name','title' ,'email', 'image', 'description','birthday','avaliable','user_images','user_accounts')

