# from django.db import models
# from apps.core.models import Table, MenuItem,Room
# from apps.employees.models import Employee

# class Order(models.Model):
#     ORDER_TYPE_CHOICES = [
#         ('table', 'Stol'),
#         ('room', 'Xona'),
#     ]
    
#     STATUS_CHOICES = [
#         ('pending', 'Kutilmoqda'),
#         ('cooking', 'Tayyorlanmoqda'),
#         ('ready', 'Tayyor'),
#         ('served', 'Yetkazildi'),
#         ('paid', 'To\'landi'),
#         ('cancelled', 'Bekor qilindi'),
#     ]
    
#     order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES)
    
#     # Stol uchun (ixtiyoriy)
#     table = models.ForeignKey(
#         Table, 
#         on_delete=models.PROTECT, 
#         related_name='orders',
#         null=True, 
#         blank=True
#     )
    
#     # Xona uchun (ixtiyoriy)
#     room = models.ForeignKey(
#         Room, 
#         on_delete=models.PROTECT, 
#         related_name='orders',
#         null=True, 
#         blank=True
#     )
    
#     employee = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='orders')
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
#     # Xona uchun qo'shimcha
#     room_hours = models.DecimalField(max_digits=4, decimal_places=1, default=0)
#     room_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
#     # Taomlar
#     total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     final_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    
#     # Mijozlar
#     customer_count = models.PositiveIntegerField(default=1)
#     customer_name = models.CharField(max_length=200, blank=True)
#     customer_phone = models.CharField(max_length=20, blank=True)
    
#     note = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     completed_at = models.DateTimeField(null=True, blank=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         if self.order_type == 'table':
#             return f"Stol #{self.table.number} - Buyurtma {self.id}"
#         return f"Xona #{self.room.number} - Buyurtma {self.id}"

#     def calculate_total(self):
#         # Taomlar summasi
#         food_total = sum(item.subtotal for item in self.items.all())
        
#         # Xona narxi (agar xona bo'lsa)
#         if self.order_type == 'room' and self.room:
#             self.room_cost = self.room.hourly_rate * self.room_hours
        
#         self.total_amount = food_total + self.room_cost
#         self.final_amount = self.total_amount - self.discount
#         self.save()
#         return self.final_amount
    

# class OrderItem(models.Model):
#     QUANTITY_TYPE_CHOICES = [
#         ('portion', 'Porsiya'),      # Stol uchun
#         ('weight', 'Og\'irlik'),      # Xona uchun (kg)
#         ('piece', 'Dona'),            # Umumiy
#         ('liter', 'Litr'),            # Ichimliklar
#     ]
    
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    
#     # Miqdor
#     quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1)
#     quantity_type = models.CharField(
#         max_length=10, 
#         choices=QUANTITY_TYPE_CHOICES,
#         default='portion'
#     )
    
#     # Narx (vaqtinchalik, o'zgarishi mumkin)
#     price_at_time = models.DecimalField(max_digits=10, decimal_places=2)
    
#     # Xona uchun og'irlik narxini hisoblash
#     weight_price_per_kg = models.DecimalField(
#         max_digits=10, 
#         decimal_places=2, 
#         default=0,
#         help_text='1 kg narxi (xona uchun)'
#     )
    
#     note = models.CharField(max_length=255, blank=True)
#     status = models.CharField(max_length=20, choices=Order.STATUS_CHOICES, default='pending')
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         unit = self.get_quantity_type_display()
#         return f"{self.menu_item.name} - {self.quantity} {unit}"

#     @property
#     def subtotal(self):
#         # Agar og'irlik bo'lsa va kg narxi ko'rsatilgan bo'lsa
#         if self.quantity_type == 'weight' and self.weight_price_per_kg > 0:
#             return self.weight_price_per_kg * self.quantity
#         return self.price_at_time * self.quantity

# class Payment(models.Model):
#     METHOD_CHOICES = [
#         ('cash', 'Naqd'),
#         ('card', 'Karta'),
#         ('transfer', 'O\'tkazma'),
#     ]
    
#     order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='payments')
#     amount = models.DecimalField(max_digits=12, decimal_places=2)
#     method = models.CharField(max_length=20, choices=METHOD_CHOICES)
#     received_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     change_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.amount} - {self.get_method_display()}"
