from django.db import models

# Create your models here.
class Employer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    department = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Employer"
        verbose_name_plural = "Employers"
