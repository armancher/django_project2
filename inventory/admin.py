from django.contrib import admin
from inventory.models import Order, Product, Tag, Inventory
from inventory.forms import InventoryForm

class OrderInline(admin.TabularInline):
    model = Order
    fields=('weight','product','user','created_at','updated_at')
    readonly_fields = ('created_at', 'updated_at')
    extra=3
    
class TagInline(admin.TabularInline):
      model =Tag.products.through
      extra=2
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'price', 'inventory')
    search_fields = ('inventory__name', 'inventory__address', 'price')
    inlines=[OrderInline,TagInline]

class InventoryAdmin(admin.ModelAdmin):
    form = InventoryForm
    list_display = ('name', 'address', 'phone_number', 'manager')
    search_fields=('name', 'address', 'phone_number', 'manager')
    fieldsets = [
        (None, {'fields': ('name', 'address', 'phone_number', 'manager')}),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Tag)