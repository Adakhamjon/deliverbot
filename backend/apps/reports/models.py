# from django.db import models

# class Expense(models.Model):
#     CATEGORY_CHOICES = [
#         ('products', 'Mahsulotlar'),
#         ('salary', 'Ish haqi'),
#         ('rent', 'Ijara'),
#         ('utilities', 'Kommunal'),
#         ('other', 'Boshqa'),
#     ]
    
#     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
#     amount = models.DecimalField(max_digits=12, decimal_places=2)
#     description = models.TextField(blank=True)
#     date = models.DateField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-date', '-created_at']

#     def __str__(self):
#         return f"{self.get_category_display()} - {self.amount} ({self.date})"


# class DailyReport(models.Model):
#     date = models.DateField(unique=True)
#     total_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     total_orders = models.PositiveIntegerField(default=0)
#     total_customers = models.PositiveIntegerField(default=0)
#     total_expenses = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     net_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering = ['-date']

#     def __str__(self):
#         return f"Hisobot {self.date}"

#     def calculate_net_profit(self):
#         self.net_profit = self.total_revenue - self.total_expenses
#         self.save()
#         return self.net_profit
