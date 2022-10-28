

from .models import Certificate
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers


class CertificatesSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'
 