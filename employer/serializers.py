from django.db.models import fields
from rest_framework import serializers
from .models import Employer


class EmployerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ("id", "name", "email", "department")
