from django.db import models
from django.contrib.auth import get_user_model

class Laptops(models.Model):
    Name = models.CharField(max_length=255)   
    Description = models.TextField(blank=True)
    Price = models.DecimalField(max_digits=6, decimal_places=2)
    Seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE )
    Date_puplished = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
