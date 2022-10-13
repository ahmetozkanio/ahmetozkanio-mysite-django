

from .models import Account, UserImage, UserModel

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = '__all__'
class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class UserModelSerializer(ModelSerializer):
    user_images = UserImageSerializer(many=True, read_only=True)
    user_accounts = UserAccountSerializer(many=True, read_only=True)
    class Meta:
        model = UserModel
        fields = ('id','user_name', 'firs_name','last_name','title' ,'email', 'image', 'description','birthday','avaliable','user_images','user_accounts')

