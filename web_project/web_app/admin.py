from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Employees)
admin.site.register(Tables)
admin.site.register(Customers)
admin.site.register(Menu)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(Reservations)
admin.site.register(Shifts)