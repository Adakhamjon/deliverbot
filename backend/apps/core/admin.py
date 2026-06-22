from django.contrib import admin
from .models import Category,MenuItem,Order,OrderItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'sort_order', 'is_active', 'created_at']
    list_editable = ['sort_order', 'is_active']
    search_fields = ['name']
    ordering = ['sort_order', 'name']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'created_at']
    list_filter = ['category', 'is_available']
    search_fields = ['name']
    list_editable = ['price', 'is_available']

class OrderItemInline(admin.TabularInline):                  
    model = OrderItem
    extra = 1


@admin.register(Order)                                       
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'phone', 'total', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['customer_name', 'phone']
    list_editable = ['status']
    inlines = [OrderItemInline]


@admin.register(OrderItem)                                  
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'menu_item', 'quantity', 'price', 'subtotal']
    list_filter = ['order']
