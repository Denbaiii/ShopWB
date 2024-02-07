from django.contrib import admin
from .models import Order, ShippingAddress, OrderItem

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
