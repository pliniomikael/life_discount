from django.db import router
from django.urls import path

from rest_framework.routers import SimpleRouter
from .views import EmployerViewset

router = SimpleRouter()
router.register("employers", EmployerViewset, basename="employers")
