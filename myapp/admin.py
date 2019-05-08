from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price', 'image')
    list_display = ('name', 'description', 'price' , 'image')
    list_filter = ('name', 'description')
    
admin.site.register(Item, ItemAdmin)