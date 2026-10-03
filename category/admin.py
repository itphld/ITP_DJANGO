from django.contrib import admin
from .models import Category
from django.utils.html import format_html
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src = {} height= 100 width = 100>' .format(object.cat_image.url))


    list_display=('category_name','description','thumbnail','is_active')
    list_editable=('is_active',)
    list_filter=('is_active',)
    prepopulated_fields={'slug':('category_name',)}
    thumbnail.short_description='Category Image'
admin.site.register(Category,CategoryAdmin)
