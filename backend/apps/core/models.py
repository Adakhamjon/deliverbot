from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sort_order', 'name']
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='items'
    )
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']
        verbose_name = 'Menyu taomi'
        verbose_name_plural = 'Menyu taomlari'

    def __str__(self):
        return f"{self.name} ({self.price})"
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Yangi'),
        ('cooking', 'Tayyorlanmoqda'),
        ('ready', 'Tayyor'),
        ('delivered', 'Yetkazildi'),
        ('cancelled', 'Bekor qilindi'),
    ]
    PAYMENT_STATUS_CHOICES = [
    ('pending', 'Kutilmoqda'),
    ('checking', 'Chek yuborilgan'),
    ('paid', 'Tasdiqlangan'),
    ('rejected', 'Rad etilgan'),
]


    customer_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    telegram_id = models.BigIntegerField(
        null=True,
        blank=True
    )

    telegram_username = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )

    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    payment_status = models.CharField(
    max_length=20,
    choices=PAYMENT_STATUS_CHOICES,default='pending'
)
    receipt = models.ImageField(
    upload_to='receipts/',
    null=True,
    blank=True
)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Buyurtma #{self.id} - {self.customer_name}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Buyurtma elementi'
        verbose_name_plural = 'Buyurtma elementlari'

    def __str__(self):
        return f"{self.menu_item.name} x{self.quantity}"

    @property
    def subtotal(self):
        return self.price * self.quantity