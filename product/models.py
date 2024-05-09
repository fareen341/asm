from django.db import models
from users.models import User
import datetime
from master.models import (Vendor, Location,
                            Category,  Branch, SoftwareType)


# SOFTWARE PRODUCT
class Software(models.Model):
    name = models.CharField(max_length=50)
    softwaretype = models.ForeignKey(SoftwareType, on_delete=models.PROTECT)
    purchased_on = models.DateField((""), auto_now=False, auto_now_add=False)
    expiry = models.DateField((""), auto_now=False, auto_now_add=False)
    installed_on = models.ForeignKey("Hardware", null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
    


# HARDWARE PRODUCT
class Hardware(models.Model):
    name = models.CharField(max_length=50)
    # brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # assettype=models.ForeignKey(Category,on_delete=models.PROTECT,null=True, related_name='asset_type1')
    asset_type=models.CharField(choices= (('IT Assets', 'IT Assets'),('Non IT Assets', 'Non IT Assets')),max_length=50,blank=True,default="IT Assets")
    # category = models.CharField(choices= (('IT Assets', 'IT Assets'),('Non IT Assets', 'Non IT Assets')),max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    barcode = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    purchased_on = models.DateField(auto_now=False, auto_now_add=False)
    warranty_expiry = models.DateField(auto_now=False, auto_now_add=False)
    tpm_expiry = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=30, choices=(
        ('working', 'working'), ('damaged', 'damaged'),('disposed', 'disposed')))
    branch= models.ForeignKey(Branch,on_delete=models.PROTECT,null=True)
    location = models.ForeignKey(Location,on_delete=models.PROTECT,null=True)
    assigned_to = models.ForeignKey(User, null=True ,blank=True, on_delete=models.PROTECT)
    cost=models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.name + " - " + self.barcode
    
    
        
    # def remaining_days(self):
    #     remaining_days = (self.warranty_expiry - self.purchased_on).days
        
    #     years = remaining_days // 365

    #     # Calculating months
    #     months = (remaining_days - years *365) // 30

    #     # Calculating days
    #     days = (remaining_days - years * 365 - months*30)
        
    #     return years,months,days
    #    

    
    
# Non IT Assets model

class Nonitasset(models.Model):
    name = models.CharField(max_length=50)
    asset_type=models.CharField(max_length=50,blank=True,default="NON IT Assets")
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    barcode = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    purchased_on = models.DateField(auto_now=False, auto_now_add=False)
    warranty_expiry = models.DateField(auto_now=False, auto_now_add=False)
    # status = models.CharField(max_length=30, choices=(
    #     ('working', 'working'), ('damaged', 'damaged'),('disposed', 'disposed')))
    branch= models.ForeignKey(Branch,on_delete=models.PROTECT,null=True)
    location = models.ForeignKey(Location,on_delete=models.PROTECT,null=True)
    assigned_to = models.ForeignKey(User, null=True ,blank=True, on_delete=models.PROTECT)
    cost=models.PositiveIntegerField(blank=True)

    def __str__(self):
        return self.name + " - " + self.barcode