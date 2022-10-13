

from .models import Project
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class ProjectSerializer(ModelSerializer):
    project_images = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = ('id','name', 'description','github_url','date' ,'image', 'avaliable', 'project_images','category')
 