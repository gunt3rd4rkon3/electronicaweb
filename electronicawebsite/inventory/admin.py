from django.contrib import admin
from .models import Category, Product, ProductInstance, Supplier


# admin.site.register(Product)
# admin.site.register(ProductInstance)
class ProductInstanceInline(admin.TabularInline):
    model = ProductInstance


# Register the Admin classes for Product using the decorator
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'supplier', 'display_category', 'stock', 'maxunits')
    inlines = [ProductInstanceInline]


# Register the Admin classes for InstanceProduct using the decorator
@admin.register(ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'register_date')

    fieldsets = (
        (None, {
            'fields': ('product', 'id'),
        }),
        ('Availability', {
            'fields': ('status', 'register_date', 'available_date', 'sinnombre')
        }),
    )


# admin.site.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'cif', 'business_email')
    fields = ['business_name', ('cif', 'business_email')]


# Register the admin class with the associated model
admin.site.register(Supplier, SupplierAdmin)

admin.site.register(Category)
