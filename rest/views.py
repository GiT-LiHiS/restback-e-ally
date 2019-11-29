from django.shortcuts import render
from rest_framework import viewsets, filters
from django.contrib.auth.models import User, Group
from .models import Clothing
from .models import Category
from .models import Brand
from .models import Promo
from .serializer import ClothingSerializer, CategorySerializer, BrandSerializer, PromoSerializer
from rest_framework import generics


# Create your views here.

class NameList(viewsets.ModelViewSet):
    serializer_class = ClothingSerializer
    queryset = Clothing.objects.all()
    lookup_field = 'itemid'


class PromoViewSet(viewsets.ModelViewSet):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ClothingViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('keywords',)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class jacketList(viewsets.ModelViewSet):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer

    def get_queryset(self):
        return Clothing.objects.filter(category__name__icontains="Jackets")


class jeansList(viewsets.ModelViewSet):
    queryset = Clothing.objects.all()
    serializer_class = ClothingSerializer

    def get_queryset(self):
        return Clothing.objects.filter(category__name__icontains="jeans")
