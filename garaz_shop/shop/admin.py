from django.contrib import admin

from .models import Categoria
from .models import Oil_product
from .models import Filter_product
from .models import Carsina_pocupok
from .models import Product
from .models import Pocupatel

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Categoria._meta.get_fields()]

@admin.register(Oil_product)
class Oil_productAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Oil_product._meta.get_fields()]

@admin.register(Filter_product)
class Filter_productAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Filter_product._meta.get_fields()]

@admin.register(Carsina_pocupok)
class Carsina_pocupokAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Carsina_pocupok._meta.get_fields()]


@admin.register(Pocupatel)
class PocupatelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pocupatel._meta.get_fields()]

