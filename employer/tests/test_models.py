import pytest
from mixer.backend.django import mixer
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestModels:
    client = APIClient()

    def test_employers(self):
        employer = mixer.blend("employer.Employer", id=1)

        assert employer.id == 1

    def test_post_employer(self):

        new = {
            "id": 1,
            "name": "Plinio Mikael",
            "email": "pliniomikael@gmail.com",
            "department": "Developer Django",
        }

        response = self.client.post("/employers/", new)
        assert response.status_code == 201
        assert response.json()["name"] == new["name"]

    def test_get_employers(self):

        response = self.client.get("/employers/")
        assert response.status_code == 200

    def test_get_employer(self):
        employer = mixer.blend("employer.Employer", id=1)

        response = self.client.get("/employers/%s/" % employer.id)
        assert response.status_code == 200

    def test_put_employer(self):
        employer = mixer.blend("employer.Employer", id=1)

        update = {
            "name": "Plinio",
            "email": "pliniom@gmail.com",
            "department": "T.I",
        }
        response = self.client.put("/employers/%s/" % employer.id, data=update)
        assert response.status_code == 200

    def test_delete_employer(self):
        employer = mixer.blend("employer.Employer", id=1)

        response = self.client.delete("/employers/%s/" % employer.id)
        assert response.status_code == 204
