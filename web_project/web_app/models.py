from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(verbose_name='Employee name', max_length=30)
    surname = models.CharField('Employee surname', max_length=30)
    position = models.CharField('Position', max_length=30)
    salary = models.DecimalField('Salary', max_digits=10, decimal_places=2)
    phone = models.CharField('Phone number', max_length=20)
    email = models.EmailField('Email', max_length=50)
    hire_date = models.DateField('Hire date')

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['surname', 'name']

    def __str__(self):
        return f"{self.surname}"
    
class Menu(models.Model):
    dish_name = models.CharField('Dish name', max_length=100)
    category = models.CharField('Category', max_length=20)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    description = models.TextField('Description')
    cooking_time = models.IntegerField('Cooking time (min)', default=15)
    is_available = models.BooleanField('Available', default=True)
    
    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Menu'
        ordering = ['category', 'dish_name']
    
    def str(self):
        return self.dish_name


class Tables(models.Model):
    STATUS_CHOICES = [
        ('free', 'Free'),
        ('occupied', 'Occupied'),
        ('reserved', 'Reserved'),
        ('maintenance', 'Maintenance'),
    ]
    
    table_number = models.IntegerField('Table number', unique=True)
    capacity = models.IntegerField('Capacity')
    status = models.CharField('Status', max_length=15, default='free')
    location = models.CharField('Location', max_length=100)
    
    class Meta:
        verbose_name = 'Table'
        verbose_name_plural = 'Tables'
        ordering = ['table_number']
    
    def str(self):
        return f"Table #{self.table_number}"

class Customers(models.Model):
    phone = models.CharField('Phone', max_length=20, unique=True)
    full_name = models.CharField('Full name', max_length=100)
    email = models.EmailField('Email', unique=True)
    total_orders = models.IntegerField('Total orders', default=0)
    total_spent = models.DecimalField('Total spent', max_digits=12, decimal_places=2)
    created_at = models.DateTimeField('Registration date', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-created_at']
    
    def str(self):
        return self.full_name or self.phone

class Orders(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('served', 'Served'),('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]
    
    table = models.ForeignKey('Tables', on_delete=models.CASCADE, verbose_name='Table')
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Employee')
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name='Customer')
    order_date = models.DateTimeField('Order date')
    status = models.CharField('Status', max_length=15, choices=STATUS_CHOICES)
    total_amount = models.DecimalField('Total price', max_digits=10, decimal_places=2, default=0)
    notes = models.TextField('Notes')
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-order_date']
    
    def str(self):
        return f"Order #{self.id}"

class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_items', verbose_name='Order')
    dish = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name='Dish')
    quantity = models.IntegerField('Quantity', default=1)
    price = models.DecimalField('Price per unit', max_digits=8, decimal_places=2)
    special_requests = models.TextField('Special request')
    
    class Meta:
        verbose_name = 'Order item'
        verbose_name_plural = 'Order item'
    
    def str(self):
        return f"{self.dish.dish_name} x {self.quantity}"

class Reservations(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    customer_name = models.CharField('Customer name', max_length=100)
    phone = models.CharField('Phone', max_length=20)
    table = models.ForeignKey('Tables', on_delete=models.CASCADE, verbose_name='Table')
    reservation_date = models.DateTimeField('Reservation date')
    guests_count = models.IntegerField('Guests count')
    status = models.CharField('Status', max_length=15, choices=STATUS_CHOICES)
    duration = models.IntegerField('Duration (min)', default=120)
    notes = models.TextField('Notes')
    
    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        ordering = ['reservation_date']
    
    def str(self):
        return f"Reservation #{self.id}"

class Shifts(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='shifts', verbose_name='Сотрудник')
    shift_date = models.DateField('Дата смены')
    start_time = models.TimeField('Время начала')
    end_time = models.TimeField('Время окончания')
    hours_worked = models.DecimalField('Отработано часов',max_digits=4,decimal_places=2)
    notes = models.TextField('Заметки')
    
    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ['-shift_date', 'start_time']
        unique_together = ['employee', 'shift_date']
    
    def str(self):
        return f"Смена {self.employee}"