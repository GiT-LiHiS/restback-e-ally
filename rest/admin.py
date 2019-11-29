from django.contrib import admin
from .models import Clothing
from .models import Category
from .models import Brand
from .models import Promo


# Register your models here.
admin.site.register(Clothing)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Promo)
