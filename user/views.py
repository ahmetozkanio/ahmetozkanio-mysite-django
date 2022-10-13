
#from rest_framework import response
#from django.http import Http404
from .models import UserModel
#from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserModelSerializer
#from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def getUser(request):
    users = UserModel.objects.all()
    serializer = UserModelSerializer(users,many= True)
    return Response(serializer.data)
