
# #from rest_framework import response
# #from django.http import Http404
# from api.serializers import ProjectModelSerializer, UserModelSerializer
# from projects.models import ProjectModel
# from user.models import UserModel
# #from django.urls import reverse
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# #from rest_framework.views import APIView

# # Create your views here.
# @api_view(['GET'])
# def getUser(request):
#     users = UserModel.objects.all()
#     serializer = UserModelSerializer(users,many= True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def getProjects(request):
#     projects = ProjectModel.objects.all()
#     serializer = ProjectModelSerializer(projects,many= True)
#     return Response(serializer.data)