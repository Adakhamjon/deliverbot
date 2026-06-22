from django.views.generic import TemplateView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from urllib import request
from .utils import (
    send_order_notification,
    send_status_notification,
    send_receipt_notification,
)
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from .models import Category, MenuItem, Order
from .serializers import (
    CategorySerializer,
    MenuItemSerializer,
    OrderSerializer,
    OrderCreateSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny] 

class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.filter(is_available=True)
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category_id=category)
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    
    def get_serializer_class(self):
        if self.action == 'create':
            
            return OrderCreateSerializer
        return OrderSerializer
    def create(self, request, *args, **kwargs):
        print("REQUEST DATA:")
        print(request.data)
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        order = serializer.save()

        return Response(
        OrderSerializer(order).data,
        status=status.HTTP_201_CREATED
    )
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get('status')
        
        if new_status in dict(Order.STATUS_CHOICES):
            order.status = new_status
            order.save()
            send_status_notification(order)
            return Response({'status': 'updated'})
        return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True, methods=['post'])
    def upload_receipt(self, request, pk=None):
        order = self.get_object()

        if 'receipt' not in request.FILES:
            return Response(
                {'error': 'Receipt file required'},
                status=400
            )

        order.receipt = request.FILES['receipt']
        order.payment_status = 'checking'
        order.save()
        send_receipt_notification(order)
        return Response({
            'status': 'uploaded'
        })


class ReactAppView(TemplateView):
    template_name = "index.html"