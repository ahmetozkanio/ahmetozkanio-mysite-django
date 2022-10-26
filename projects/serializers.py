

from .models import Project, ProjectImage, ProjectTool
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class ProjectImagesSerializer(ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = '__all__'

class ProjectToolsSerializer(ModelSerializer):
    class Meta:
        model = ProjectTool
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    project_tools = ProjectToolsSerializer(many=True, read_only=True)
    project_images = ProjectImagesSerializer(many=True, read_only=True)
   
    class Meta:
        model = Project
        fields = ('id','name', 'description','github_url','date' ,'image', 'avaliable', 'category','project_images','project_tools',)
 