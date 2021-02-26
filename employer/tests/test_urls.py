from django.test import Client

from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestUrls:
    def test_employers_url(self):

        response = Client().get("/employers/")

        assert response.status_code == 200

    def test_employer_url(self):
        employer = mixer.blend("employer.Employer", id=1)

        response = Client().get("/employers/%s/" % employer.id)
        assert response.status_code == 200