from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import secrets
# Create your models here.

CATEGORY_CHOICES ={
    ('TL', 'Tele'),
    ('RD', 'Radio'),
    ('PH', 'Phone'),
    ('LT', 'Laptop'),
    ('WT', 'Watch'),
    ('FT', 'Fruit'),
    ('SH', 'shoes'),
}



STATE_CHOICES = {

('Abia', 'Abia'),
('Adamawa', 'Adamawa'),
('Akwa Ibom', 'Akwa Ibom'),
('Anambra', 'Anambra'),
('Bauchi', 'Bauchi'),
('Bayelsa', 'Bayelsa'),
('Benue', 'Benue'),
('Borno', 'Borno'),
('Cross River', 'Cross River'),
('Delta', 'Delta'),
('Ebonyi', 'Ebonyi'),
('Edo', 'Edo'),
('Ekiti', 'Ekiti'),
('Enugu', 'Enugu'),
('Gombe', 'Gombe'),
('Imo', 'Imo'),
('Jigawa', 'Jigawa'),
('Kaduna', 'Kaduna'),
('Kano', 'Kano'),
('Katsina', 'Katsina'),
('Kebbi', 'Kebbi'),
('Kogi', 'Kogi'),
('Kwara', 'Kwara'),
('Lagos', 'Lagos'),
('Nasarawa', 'Nasarawa'),
('Niger', 'Niger'),
('Ogun', 'Ogun'),
('Ondo', 'Ondo'),
('Osun', 'Osun'),
('Oyo', 'Oyo'),
('Plateau', 'Plateau'),
('Rivers', 'Rivers'),
('Sokoto', 'Sokoto'),
('Taraba', 'Taraba'),
('Yobe', 'Yobe'),
('Zamfara', 'Zamfara'),
('FCT', 'FCT')

}



class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField()
    prodapp = models.TextField(default="")
    category= models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to="product")


    def __str__(self):
        return self.title



class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)


    @property
    def total_cost(self):
        return self.quantity + self.product.discounted_price
    

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length = 200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.amount}'


    def save(self, *args, **kwargs):
        while not self.ref:
            ref = secrets.token_urlsafe(50)
            object_with_similar_ref = Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args, **kwargs)

    
    def amount_value(self):
        return int(self.amount) * 100
    


        
    
STATUS_CHOICES ={
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("Delivered", "Delivered"),
    ("Cancel", "Cancel"),
    ("Pending", "Pending"),
}

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="", related_name='orders')

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)