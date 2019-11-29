"""ethicallyrest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest import views
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router2 = routers.DefaultRouter()
router.register(r'promo', views.PromoViewSet)
router.register(r'brand', views.BrandViewSet)
router.register(r'clothing', views.ClothingViewSet)
router.register(r'category', views.CategoryViewSet)
router2.register(r'jacket', views.jacketList)
router2.register(r'jeans', views.jeansList)
router.register(r'itemname', views.NameList)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('categories/', include(router2.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROUTE)
