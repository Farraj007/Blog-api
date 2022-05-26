from rest_framework import serializers
from permision.models import Laptops

class LaptopsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Laptops
        fields = ('id', 'Name', 'Description', 'Price', 'Seller', 'Date_puplished', 'updated')