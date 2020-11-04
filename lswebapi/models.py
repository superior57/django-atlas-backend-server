from django.db import models
from django.contrib.auth.models import User

class ProductDetails(models.Model):
	id = models.IntegerField(unique=True,primary_key=True)
	product_id = models.IntegerField()
	product_name = models.CharField(max_length=64)
	product_description = models.TextField(max_length=256)
	purchase_date = models.DateField()

class UserDetails(models.Model):
        user_id = models.AutoField(primary_key=True)
        first_name = models.CharField(max_length=64)
        last_name = models.CharField(max_length=64)
        phone = models.CharField(max_length=16)
        date_added = models.DateField()

