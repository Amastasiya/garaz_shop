from django.contrib import admin

from .models import Pocupatel
from .models import Categoria
from .models import Product
from .models import Oil_product
from .models import Filter_product
from .models import Carsina


@admin.register(Pocupatel)
class PocupatelAdmin(admin.ModelAdmin):
    #exclude = ['carsina']
    list_display = list(
        set([field.name for field in Pocupatel._meta.get_fields()]) - set([
            'carsina', 'categoria'
        ]))

    print('POCUPATEL', list_display)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = list(
        set([field.name for field in Categoria._meta.get_fields()]) - set([
            'carsina', 'product'
        ]))

@admin.register(Oil_product)
class Oil_productAdmin(admin.ModelAdmin):
    list_display = list(
        set([field.name for field in Oil_product._meta.get_fields()]) - set([
            'carsina'
        ]))

@admin.register(Filter_product)
class Filter_productAdmin(admin.ModelAdmin):
    list_display = list(
        set([field.name for field in Filter_product._meta.get_fields()]) - set([
            'carsina'
        ]))


@admin.register(Carsina)
class CarsinaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Carsina._meta.get_fields()]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = list(
        set([field.name for field in Product._meta.get_fields()]) - set([
            'carsina', 'categoria', 'oil_product', 'filter_product'
        ]))
    print("\n\n\nPRODUCT " + str(list_display))

