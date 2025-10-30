from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property, Rent, Buy, shortlet, Land


# When Property is added/updated/deleted
@receiver([post_save, post_delete], sender=Property)
def clear_property_cache(sender, **kwargs):
    cache.delete('property')


@receiver([post_save, post_delete], sender=Rent)
def clear_rent_cache(sender, **kwargs):
    cache.delete('rent')


@receiver([post_save, post_delete], sender=Buy)
def clear_buy_cache(sender, **kwargs):
    cache.delete('buy')


@receiver([post_save, post_delete], sender=shortlet)
def clear_shortlet_cache(sender, **kwargs):
    cache.delete('shortlet')


@receiver([post_save, post_delete], sender=Land)
def clear_land_cache(sender, **kwargs):
    cache.delete('land')
