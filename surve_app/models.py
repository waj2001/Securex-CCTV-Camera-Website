from django.db import models

# Create your models here.

class employee_db(models.Model):
    image = models.ImageField(upload_to="Emp_photo")
    emp_name = models.CharField(max_length=100)
    emp_desg = models.CharField(max_length=150)
    emp_exp = models.IntegerField()

    def __str__(self):
        return self.emp_name

class ourservices(models.Model):
    img = models.ImageField(upload_to="Emp_services")
    title = models.CharField(max_length=300)
    descr = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=14)
    services = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    