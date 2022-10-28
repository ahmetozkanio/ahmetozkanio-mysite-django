
from certificates.models import Certificate
from certificates.serializers import CertificatesSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def getCertificates(request):
    projects = Certificate.objects.all()
    serializer = CertificatesSerializer(projects,many= True)
    return Response(serializer.data)