from permision.api.viewset import LaptopsListView, LaptopsDetailView
from django.urls import path

urlpatterns = [
    path('', LaptopsListView.as_view(),name='Laptops_list'),
    path('laptops-list/<int:pk>', LaptopsDetailView.as_view(), name='Laptops_detail'),
]
