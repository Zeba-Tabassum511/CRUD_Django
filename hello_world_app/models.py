from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length = 100)

class data(models.Model):
    name = models.CharField(max_length=100,null=True)
    brand_name = models.CharField(max_length=100,null=True)
    regular_price_value =models.CharField(max_length=60,null=True)
    offer_price_value = models.CharField(max_length=60,null=True)
    currency = models.CharField(max_length=60,null=True)
    classification_l1 = models.CharField(max_length=60,null=True)
    classification_l2 = models.CharField(max_length=60,null=True)
    classification_l3 = models.CharField(max_length=60,null=True)
    classification_l4 = models.CharField(max_length=60,null=True)
    image_url = models.CharField(max_length=60,null=True)