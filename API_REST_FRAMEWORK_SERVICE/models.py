from django.db import models

# Create your models here.
class Products_Fake(models.Model):
    product_image = models.ImageField(null=True, upload_to='products/')
    product_name = models.CharField(max_length=200, null=True)
    product_price = models.IntegerField( null=True)
    product_description = models.TextField(null=True)
    product_rating = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    product_deler = models.TextField(max_length=200, null=True)
    product_category = models.CharField(max_length=200, null=True)
 
    def __str__(self):
        return f"PRODUCT NAME :{self.product_name}, PRODUCT PRICE :{self.product_price}"