from django.db import models

class ProductData(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=100)
    product_cost=models.IntegerField()
    product_class=models.CharField(max_length=100)
    product_color=models.CharField(max_length=100)
    no_of_products=models.IntegerField()
    mfg_date=models.DateField(max_length=100)
    exp_date=models.DateField(max_length=100)
    customer_name=models.CharField(max_length=100)
    mobile_number=models.BigIntegerField()
    email_id=models.EmailField(max_length=100)
