from re import I
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from .models import Employer
from .serializers import EmployerSerializers


class EmployerViewset(ModelViewSet):
    """
    API to employers
    """

    queryset = Employer.objects.all().order_by("-id")
    serializer_class = EmployerSerializers
