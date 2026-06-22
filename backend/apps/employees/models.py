# from django.db import models
# from django.contrib.auth.models import User

# class EmployeeRole(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#     can_take_orders = models.BooleanField(default=False)
#     can_manage_kitchen = models.BooleanField(default=False)
#     can_manage_cashier = models.BooleanField(default=False)
#     can_view_reports = models.BooleanField(default=False)
#     can_manage_inventory = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name


# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     role = models.ForeignKey(EmployeeRole, on_delete=models.PROTECT)
#     full_name = models.CharField(max_length=200)
#     phone = models.CharField(max_length=20, blank=True)
#     pin_code = models.CharField(max_length=10, unique=True, help_text='Kirish kodi')
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['full_name']

#     def __str__(self):
#         return f"{self.full_name} ({self.role})"
