
# from projects.models import ProjectModel
# from user.models import UserImagesModel, UserModel

# from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers


# class UserImagesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserImagesModel
#         fields = ['id', 'user', 'images']
# class UserAccountsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserImagesModel
#         fields = ['id', 'user', 'images']

# class UserModelSerializer(ModelSerializer):
#     user_images = UserImagesSerializer(many=True, read_only=True)
#     user_accounts = serializers.StringRelatedField(many=True)
#     class Meta:
#         model = UserModel
#         fields = ('id','user_name', 'firs_name','last_name','title' ,'email', 'image', 'description','birthday','avaliable','user_images','user_accounts')

