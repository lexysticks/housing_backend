from django.apps import AppConfig


class HouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'house'
    
    def ready(self):
        import house.signals
        return super().ready()
    
    
# from django.apps import AppConfig


# class RealestateConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'house'  # your app name

#     def ready(self):
#         import house.signals
