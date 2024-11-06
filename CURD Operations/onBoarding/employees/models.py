from django.db import models

# Create your models here.


class Employee(models.Model):
    idemp = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    contact = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'emp'
