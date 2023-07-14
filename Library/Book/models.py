from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email=models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","first_name","last_name"]

    def __str__(self):
        return self.email

class Book(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField(max_length=400)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    price= models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.title
# Create your models here.
