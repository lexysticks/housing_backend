from django.contrib import admin
from . models import Property,Rent,Land,Buy,shortlet,ContactMessage
# Register your models here.
admin.site.register(Property)
admin.site.register(Rent)
admin.site.register(Land)
admin.site.register(Buy)
admin.site.register(shortlet)
admin.site.register(ContactMessage)