from rest_framework import serializers
from .models import Clothing
from .models import Category
from .models import Brand
from .models import Promo


class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ClothingSerializer(serializers.ModelSerializer):
    # Return serialize brand and clothing as a object instead of number
    category = CategorySerializer(read_only=True)
    Brand = BrandSerializer(read_only=True)

    class Meta:
        model = Clothing
        fields = '__all__'
