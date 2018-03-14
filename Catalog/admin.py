from django.contrib import admin
from Catalog.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name']


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subcategory._meta.fields]
    exclude = ["Prise", "Quantity"]

    class Meta:
        model = Subcategory


class GoogAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Data', 'Price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Good, GoogAdmin)