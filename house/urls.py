
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet,LandViewSet,ShortletViewSet,BuyViewSet,RentViewSet

router = DefaultRouter()
router.register('properties', PropertyViewSet, basename='property')
router.register('Lands', LandViewSet, basename='Lands')
router.register('shortlet', ShortletViewSet, basename='shortlet')
router.register('buy', BuyViewSet, basename='buy')
router.register('rent', RentViewSet, basename='rent')

urlpatterns = [
    path('', include(router.urls)),
]
