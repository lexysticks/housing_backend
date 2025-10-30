from rest_framework import serializers
from .models import Property, Rent, Buy, shortlet, Land, ContactMessage


class PropertySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = '__all__'

    def get_image_url(self, obj):
        try:
            return obj.images.url
        except:
            return None


class RentSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Rent
        fields = '__all__'

    def get_image_url(self, obj):
        try:
            return obj.images.url
        except:
            return None


class BuySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Buy
        fields = '__all__'

    def get_image_url(self, obj):
        try:
            return obj.images.url
        except:
            return None


class ShortletSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = shortlet
        fields = '__all__'

    def get_image_url(self, obj):
        try:
            return obj.images.url
        except:
            return None


class LandSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Land
        fields = '__all__'

    def get_image_url(self, obj):
        try:
            return obj.images.url
        except:
            return None


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
