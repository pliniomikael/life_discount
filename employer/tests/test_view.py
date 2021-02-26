from http import HTTPStatus
from django.test import TestCase, RequestFactory

from employer.views import EmployerViewset
from rest_framework.test import APIClient

import pytest


@pytest.mark.django_db
class TestViews(TestCase):
    client = APIClient()
    factory = RequestFactory()

    def test_employer_viewset_get(self):
        request = self.factory.get("/employers/")
        response = EmployerViewset.as_view({"get": "list"})(request)
        print(response)

        self.assertEqual(response.status_code, HTTPStatus.OK._value_)

    def test_employer_viewset_post(self):
        client = APIClient()
        new = {
            "id": 1,
            "name": "Plinio Mikael",
            "email": "pliniomikael@gmail.com",
            "department": "Developer Django",
        }
        response = client.post("/employers/", data=new)

        self.assertEqual(response.status_code, HTTPStatus.CREATED._value_)
