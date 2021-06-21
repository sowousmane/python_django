from django.contrib import admin
from ecom.models import Product, Category, Customer, Order, ShippinngAdress, OrderedItem


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('available', 'created', 'updated',)
    list_display = (
        'name',
        'image',
        'description',
        'price',
        'available',
        'created',
        'updated'
    )


admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(ShippinngAdress)
admin.site.register(OrderedItem)
