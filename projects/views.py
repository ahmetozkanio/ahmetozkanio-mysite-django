from django.shortcuts import render

from .models import Project
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(['GET'])
def getProjects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects,many= True)
    return Response(serializer.data)