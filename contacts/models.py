from django.db import models


class Contacts(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
