from django.contrib import admin
from AppDemo.models import Producto

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'talla', 'valor']

    
admin.site.register(Producto, ProductoAdmin)