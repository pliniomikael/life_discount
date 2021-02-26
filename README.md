[![codecov](https://codecov.io/gh/pliniomikael/life_discount/branch/main/graph/badge.svg?token=D5VE7UY08O)](https://codecov.io/gh/pliniomikael/life_discount)
<img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/pliniomikael/life_discount/Django%20CI">
<h1 align="center">
    <img alt="DevRadar" title="#delicinha" src="https://thiagorodrigo.com.br/images/avidaefeitadedesconto-logo.png" width="200px" />
</h1>

Python and Django Developer Challenge, for the site [A vida é feita de desconto](https://thiagorodrigo.com.br/)




## :hammer: Installation

Python >= 3.0 


Within the project folder run the following commands


Installation of packages:
```
pip install -r requirements.txt
```

Run Tests:

```
py.test
```
Run Migrations:

```
python manage.py makemigrations
```
Run  Migrate:

```
python manage.py migrate
```
Create User Admin:

```
python manage.py createsuperuser
```
Run Server:

```
python manage.py runserver
```
List all employers to API:

```
curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/employers/
```
Create employers to API:

```
curl -X POST -d name=new -d email=new@example.com -d department=other -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/employers/
```

Update employers to API, do not forget pass to ID employer:

```
curl -X PUT -d id=17 -d name=new2 -d email=new2@example.com -d department=other2 -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/employers/{ID}/
```

Delete employers to API:

```
curl -X DELETE http://127.0.0.1:8000/employers/{ID}/
```
