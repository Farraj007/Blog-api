from rest_framework.generics import (
                            ListCreateAPIView,    
                            RetrieveUpdateDestroyAPIView,)
from permision.models import Laptops 
from .serializers import LaptopsSerializer    
from .permissions import IsOwnerOrReadOnly            

class LaptopsListView(ListCreateAPIView):
    queryset = Laptops.objects.all()
    serializer_class = LaptopsSerializer
    


class LaptopsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Laptops.objects.all()
    serializer_class = LaptopsSerializer
    permission_classes = (IsOwnerOrReadOnly,)