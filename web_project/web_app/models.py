from django.db import models

# Create your models here.

class Employees(models.Model):
    name = models.CharField(verbose_name='Имя сотрудника', max_length=30)
    surname = models.CharField('Фамилия сотрудника', max_length=30)
    position = models.CharField('Должность', max_length=30)
    salary = models.DecimalField('Зарплата', max_digits=10, decimal_places=2)
    phone = models.CharField('Номер телефона', max_length=20)
    email = models.EmailField('Mail', max_length=50)
    hire_date = models.DateField('Дата приема')

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['surname', 'name']

    def __str__(self):
        return f"{self.surname}"
    
class Menu(models.Model):
    dish_name = models.CharField('Название блюда', max_length=100)
    category = models.CharField('Категория', max_length=20)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)
    description = models.TextField('Описание')
    cooking_time = models.IntegerField('Время приготовления (мин)', default=15)
    is_available = models.BooleanField('Доступно', default=True)
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Меню'
        ordering = ['category', 'dish_name']
    
    def str(self):
        return self.dish_name


class Tables(models.Model):
    STATUS_CHOICES = [
        ('free', 'Свободен'),
        ('occupied', 'Занят'),
        ('reserved', 'Забронирован'),
        ('maintenance', 'На обслуживании'),
    ]
    
    table_number = models.IntegerField('Номер столика', unique=True)
    capacity = models.IntegerField('Вместимость')
    status = models.CharField('Статус', max_length=15, default='free')
    location = models.CharField('Расположение', max_length=100)
    
    class Meta:
        verbose_name = 'Столик'
        verbose_name_plural = 'Столики'
        ordering = ['table_number']
    
    def str(self):
        return f"Столик #{self.table_number}"

class Customers(models.Model):
    phone = models.CharField('Телефон', max_length=20, unique=True)
    full_name = models.CharField('ФИО', max_length=100)
    email = models.EmailField('Email', unique=True)
    total_orders = models.IntegerField('Всего заказов', default=0)
    total_spent = models.DecimalField('Всего потрачено', max_digits=12, decimal_places=2)
    created_at = models.DateTimeField('Дата регистрации', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['-created_at']
    
    def str(self):
        return self.full_name or self.phone

class Orders(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Принят'),
        ('preparing', 'Готовится'),
        ('ready', 'Готов'),
        ('served', 'Подано'),('paid', 'Оплачен'),
        ('cancelled', 'Отменен'),
    ]
    
    table = models.ForeignKey('Tables', on_delete=models.CASCADE, verbose_name='Столик')
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Сотрудник')
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE, verbose_name='Клиент')
    order_date = models.DateTimeField('Дата заказа')
    status = models.CharField('Статус', max_length=15, choices=STATUS_CHOICES)
    total_amount = models.DecimalField('Общая сумма', max_digits=10, decimal_places=2, default=0)
    notes = models.TextField('Примечания')
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-order_date']
    
    def str(self):
        return f"Заказ #{self.id}"

class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_items', verbose_name='Заказ')
    dish = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name='Блюдо')
    quantity = models.IntegerField('Количество', default=1)
    price = models.DecimalField('Цена за единицу', max_digits=8, decimal_places=2)
    special_requests = models.TextField('Особые пожелания')
    
    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'
    
    def str(self):
        return f"{self.dish.dish_name} x {self.quantity}"

class Reservations(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Подтверждено'),
        ('pending', 'Ожидание'),
        ('cancelled', 'Отменено'),
        ('completed', 'Завершено'),
    ]
    
    customer_name = models.CharField('Имя клиента', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    table = models.ForeignKey('Tables', on_delete=models.CASCADE, verbose_name='Столик')
    reservation_date = models.DateTimeField('Дата бронирования')
    guests_count = models.IntegerField('Количество гостей')
    status = models.CharField('Статус', max_length=15, choices=STATUS_CHOICES)
    duration = models.IntegerField('Продолжительность (мин)', default=120)
    notes = models.TextField('Примечания')
    
    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        ordering = ['reservation_date']
    
    def str(self):
        return f"Бронь #{self.id}"

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