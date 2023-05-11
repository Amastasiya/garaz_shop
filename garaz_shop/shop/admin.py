from django.contrib import admin

from .models import *

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Product._meta.get_fields()]

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Oil)
admin.site.register(Filter)
admin.site.register(Order)