from rest_framework import viewsets, permissions
from django.core.cache import cache
from rest_framework.response import Response
from .models import Property, Rent, Buy, shortlet, Land, ContactMessage
from .serializers import (
    PropertySerializer, RentSerializer, BuySerializer,
    ShortletSerializer, LandSerializer, ContactMessageSerializer
)


class ReadOnlyBase(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]


class PropertyViewSet(ReadOnlyBase):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        cached_data = cache.get('property')
        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set('property', data, timeout=None)
        return Response(data)


class RentViewSet(ReadOnlyBase):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer

    def list(self, request, *args, **kwargs):
        cached_data = cache.get('rent')
        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set('rent', data, timeout=None)
        return Response(data)


class BuyViewSet(ReadOnlyBase):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer

    def list(self, request, *args, **kwargs):
        cached_data = cache.get('buy')
        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set('buy', data, timeout=None)
        return Response(data)


class ShortletViewSet(ReadOnlyBase):
    queryset = shortlet.objects.all()
    serializer_class = ShortletSerializer

    def list(self, request, *args, **kwargs):
        cached_data = cache.get('shortlet')
        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set('shortlet', data, timeout=None)
        return Response(data)


class LandViewSet(ReadOnlyBase):
    queryset = Land.objects.all()
    serializer_class = LandSerializer

    def list(self, request, *args, **kwargs):
        cached_data = cache.get('land')
        if cached_data:
            return Response(cached_data)

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data

        cache.set('land', data, timeout=None)
        return Response(data)


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

