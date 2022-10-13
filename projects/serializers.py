

from .models import ProjectModel
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers



class ProjectModelSerializer(ModelSerializer):
    project_images = serializers.StringRelatedField(many=True)
    class Meta:
        model = ProjectModel
        fields = ('id','name', 'description','github_url','date' ,'image', 'avaliable', 'project_images')
 