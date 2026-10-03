from django.contrib import admin
from .models import Product
from django.utils.html import format_html
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src={} height=40> '.format(object.product_image.url))
    list_display=('thumbnail','product_name','description','price','is_available')
    prepopulated_fields={'slug':('product_name',)}
    list_filter=('price','is_available')
    list_editable=('is_available',)
    list_display_links=('thumbnail','product_name','description','price')
admin.site.register(Product,ProductAdmin)
