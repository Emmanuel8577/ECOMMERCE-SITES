from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from . models import  OrderPlaced, Payment, Product, Customer, Cart, Wishlist
from django.contrib.auth.models import Group
# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'discounted_price', 'category', 'product_image' ]


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'locality', 'city', 'state', 'zipcode']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
     list_display = ['user', 'product', 'quantity']
     def products(self, obj):
          link = reverse("admin:app_product_change", args=[obj.product.pk])
          return format_html('<a href="{}">{}</a>',link, obj.product.title)
     
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
     list_display = ['user', 'amount', 'ref', 'email', 'verified', 'timestamp']

@admin.register(OrderPlaced)
class PaymentModelAdmin(admin.ModelAdmin):
     list_display = ['user', 'customers', 'product', 'quantity', 'ordered_date', 'status', 'payment']
     def customers(self, obj):
          link = reverse("admin:app_product_change", args=[obj.customer.pk])
          return format_html('<a href="{}">{}</a>',link, obj.product.title)
     
     def products(self, obj):
          link = reverse("admin:app_product_change", args=[obj.product.pk])
          return format_html('<a href="{}">{}</a>',link, obj.product.title)
     
     def payment(self, obj):
          link = reverse("admin:app_product_change", args=[obj.payment.pk])
          return format_html('<a href="{}">{}</a>',link, obj.product.title)
     
@admin.register(Wishlist)
class PaymentModelAdmin(admin.ModelAdmin):
     list_display = ['user', 'product']
     def products(self, obj):
          link = reverse("admin:app_product_change", args=[obj.product.pk])
          return format_html('<a href="{}">{}</a>',link, obj.product.title)


admin.site.unregister(Group)