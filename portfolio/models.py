from django.db import models
from django.core.validators import MinLengthValidator

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField(validators=[MinLengthValidator(100)])

    def __str__(self):
        return f"{self.name} - {self.email}"

# Create your models here.
# class Task(models.Model):
#     # attributes
#     title = models.CharField(max_length=100)
#     completed = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

# class Book(models.Model):
#     title = models.CharField(max_length=200,unique=True)
#     author = models.CharField(max_length=100)
#     published_date = models.DateField()

#     def __str__(self):
#         return self.title
