from django.shortcuts import render

from .models import ProjectModel
from .serializers import ProjectModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def getProjects(request):
    projects = ProjectModel.objects.all()
    serializer = ProjectModelSerializer(projects,many= True)
    return Response(serializer.data)