from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username


def create_customer(sender, **kwargs):
    if kwargs['created']:
        customer = Customer.objects.create(user=kwargs['instance'])


post_save.connect(create_customer, sender=User)


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('Short', 'Short'),
        ('Tank Top', 'Tank Top'),
        ('T Shirt', 'T Shirt'),
        ('Under Wear', 'Under Wear')
    )
    name = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=255, null=True, choices=CATEGORY)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField()
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('Cancel', 'Cancel'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    OPTION = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('XLarge', 'XLarge'),
    )
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    option = models.TextField(max_length=200, null=True, blank=True, choices=OPTION)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingInformation(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=11, null=True)
    order_date = models.DateField(verbose_name=('Order Date'))

    def __str__(self):
        return str(self.address)
