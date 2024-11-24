from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','category','price','images','stock')
    prepopulated_fields = {"slug" : ("product_name",)}


admin.site.register(Product,ProductAdmin)
