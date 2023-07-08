from django.contrib import admin
from .models import *

admin.site.register(MeasureUnit)
class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id','description',)


admin.site.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id','desciption',)

admin.site.register(Indicator)

admin.site.register(Product)

