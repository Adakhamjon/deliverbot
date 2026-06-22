from rest_framework import serializers
from .models import Category, MenuItem, Order, OrderItem
from .utils import send_order_notification,send_status_notification
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'sort_order']


class MenuItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'image', 'category', 'category_name', 'is_available']


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item_name = serializers.CharField(source='menu_item.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'menu_item_name', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'customer_name', 'phone', 'address',
            'total', 'status', 'status_display','payment_status','receipt',
            'items', 'created_at'
        ]
class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            'menu_item',
            'quantity'
        ]

class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'customer_name',
            'phone',
            'address',
            'telegram_id',
            'telegram_username',
            'items'
        ]

    def create(self, validated_data):
        items_data = validated_data.pop('items')

        order = Order.objects.create(
            customer_name=validated_data['customer_name'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            telegram_id=validated_data.get('telegram_id'),
            telegram_username=validated_data.get('telegram_username', ''),
            total=0,
            status='new'
        )

        total = 0

        for item_data in items_data:
            menu_item = item_data['menu_item']
            quantity = item_data['quantity']

            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
                price=menu_item.price
            )

            total += menu_item.price * quantity

        order.total = total
        order.save()
        send_order_notification(order)

        return order