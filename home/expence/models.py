from django.db import models
from userauth.models import CustomUser
    
class Main(models.Model):
    purchased_date = models.DateField()
    location = models.CharField(max_length=100)
    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=7,decimal_places=2)
    
    def __str__(self):
        return f"purchase {self.id } on {self.purchased_date} by {self.customer.username}"
    
    
class PurchasedItem(models.Model):
    purchase = models.ForeignKey(Main,related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f"{self.name}(x{self.quantity})"