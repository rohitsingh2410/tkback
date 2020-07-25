from django.db import models
import datetime
# Create your models here.

class Categories(models.Model):
    category_name = models.CharField(max_length=30)

class Leads(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_username = models.CharField(max_length=30)
    customer_phone = models.CharField(max_length=30)
    # 0=not converted, 1=converted, 2 = Processing ,3=Fresh Lead
    lead_converted = models.IntegerField(default=3)
    lead_time = models.DateTimeField(default=datetime.datetime.utcnow())
    lead_category = models.CharField(max_length=30)
    lead_isactive = models.BooleanField(default=True)
