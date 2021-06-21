from django.conf.urls import url
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{name} - {image} , {description} {price} ({available} {created} {updated})'.format(
            name=self.name,
            image=self.get_image_display(),
            description=self.get_description_display(),
            price=self.price,
            available=self.available,
            created=self.created,
            updated=self.updated,

        )

    def get_image_display(self):
        return self.image

    def get_description_display(self):
        return self.description

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ' '
        return url


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, default="Ousmane")
    email = models.CharField(max_length=200, default="Ousmane@gmail.com")

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_orderd = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


    @property
    def get_cart_total(self):
        orderitems = self.orderitem.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def total_cart_items(self):
        orderitems = self.orderitem.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderedItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True, related_name= 'orderitem')
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippinngAdress(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
