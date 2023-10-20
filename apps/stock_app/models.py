from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

categories=(('laptops','Laptops'),
            ('desktops','Desktops'),
            ('phones','Phones'),
            ('accessories','Accessories')
            )
class Product_Model(models.Model):
    product_name=models.CharField(max_length=230,editable=True,null=True,blank=True)
    items_instock=models.PositiveBigIntegerField(default=1,editable=True)
    category=models.CharField(max_length=100,choices=categories,default='laptops',null=True,blank=True)
    unit_price=models.FloatField()
    mgf_date=models.DateField()
    expiry_date=models.DateField()
    selling_price=models.FloatField(editable=True,null=True)
    sold_on=models.DateField(auto_now_add=True, null=True)
    qty_sold=models.PositiveBigIntegerField(null=True,blank=True)
    sold_by=models.CharField(max_length=230,blank=True,null=True, help_text="Your Names")
    time_of_order=models.DateField(null=True,auto_now=True)
    product_image=models.ImageField(upload_to="product_images/",null=True,blank=True)
    description=models.TextField(default='Nice Product',null=True,blank=True)
  

    def __str__(self) -> str:
        return f"{self.product_name}"
    
    def calculate_profit(self):
        if self.qty_sold is not None and self.selling_price is not None and self.unit_price is not None:
            return self.qty_sold * ( self.selling_price - self.unit_price)
        return 0
    




class Purchase_History(models.Model):
    product = models.ForeignKey(Product_Model, on_delete=models.CASCADE)
    quantity_added = models.PositiveBigIntegerField()
    purchase_date = models.DateField(auto_now_add=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate purchases with users (optional)

class Sales_History(models.Model):
    product=models.ForeignKey(Product_Model,on_delete=models.CASCADE)
    quantity_sold=models.PositiveBigIntegerField()
    sold_on=models.DateField(auto_now_add=True)

class Profitability(models.Model):
    product=models.ForeignKey(Product_Model,on_delete=models.CASCADE)
    qty=models.ForeignKey(Sales_History,on_delete=models.CASCADE)

    def calculate_profit(self):
        if self.qty.quantity_sold is not None and self.product.selling_price is not None and self.product.unit_price is not None:
            return self.qty.quantity_sold * ( self.product.selling_price - self.product.unit_price)
        return 0
    





 
   