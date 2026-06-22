# from django.db import models
# from apps.core.models import MenuItem

# class Ingredient(models.Model):
#     UNIT_CHOICES = [
#         ('kg', 'Kilogramm'),
#         ('g', 'Gramm'),
#         ('l', 'Litr'),
#         ('ml', 'Millilitr'),
#         ('pc', 'Dona'),
#         ('pack', 'Qadoq'),
#     ]
    
#     name = models.CharField(max_length=200, unique=True)
#     unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
#     min_stock = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} ({self.get_unit_display()})"


# class MenuItemIngredient(models.Model):
#     menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='ingredients')
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
#     quantity = models.DecimalField(max_digits=10, decimal_places=3)

#     class Meta:
#         unique_together = ['menu_item', 'ingredient']

#     def __str__(self):
#         return f"{self.menu_item.name} - {self.ingredient.name}"


# class Stock(models.Model):
#     ingredient = models.OneToOneField(Ingredient, on_delete=models.CASCADE, related_name='stock')
#     quantity = models.DecimalField(max_digits=12, decimal_places=3, default=0)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.ingredient.name}: {self.quantity} {self.ingredient.get_unit_display()}"

#     @property
#     def is_low(self):
#         return self.quantity <= self.ingredient.min_stock


# class StockTransaction(models.Model):
#     TYPE_CHOICES = [
#         ('in', 'Kirim'),
#         ('out', 'Chiqim'),
#         ('adjustment', 'Tuzatish'),
#     ]
    
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT, related_name='transactions')
#     type = models.CharField(max_length=20, choices=TYPE_CHOICES)
#     quantity = models.DecimalField(max_digits=12, decimal_places=3)
#     note = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-created_at']

#     def __str__(self):
#         return f"{self.ingredient.name} - {self.type} {self.quantity}"
