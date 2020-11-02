from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Restaurant(models.Model):

    PIZZA = 1
    SAVOYARD = 2
    MEAT = 3
    FAST = 4
    GASTRO = 5
    ASIAN = 6
    MODERN = 7
    BURGER = 8
    FONDU = 9
    ITALIAN = 10
    SNACK = 11
    FRENCH = 12
    ALSACIEN = 13
    MEDITERANEEN = 14
    WINE_BAR = 15
    TAPAS = 16

    CATEGORY_CHOICES = (
        (PIZZA, "Pizza"),
        (SAVOYARD, "Savoyard"),
        (MEAT, "Meat"),
        (FAST, "Fast-food"),
        (GASTRO, "Gastro"),
        (ASIAN, "Fast-food"), 
        (MODERN, "Fast-food"),
        (BURGER, "Fast-food"),
        (FONDU, "Fast-food"),
        (ITALIAN, "Fast-food"),
        (SNACK, "Fast-food"),
        (FRENCH, "Fast-food"),
        (ALSACIEN, "Fast-food"),
        (MEDITERANEEN, "Fast-food"),
        (WINE_BAR, "Fast-food"),
        (TAPAS, "Fast-food"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='restaurant')
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='restaurant_logo/', blank=False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.det_full_name()

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver')
    avatar = models.CharField(max_length=500)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.user.det_full_name()

class Meal(models.Model):
    STARTER = 1
    MAIN_COURSE = 2
    DESSERT = 3

    CATEGORY_CHOICES = (
        (STARTER, "Starter"),
        (MAIN_COURSE, "Main course"),
        (DESSERT, "Dessert"),
    )
    restaurant = models.ForeignKey(Restaurant)
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    name = models.CharField(max_length=500)
    short_description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='meal_images/', blank=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    COOKING = 1
    READY = 2
    ONTHEWAY = 3
    DELIVERED = 4

    STATUS_CHOICES = (
        (COOKING, "Cooking"),
        (READY, "Ready"),
        (ONTHEWAY, "On the way"),
        (DELIVERED, "Delivered"),
    )

    customer = models.ForeignKey(Customer)
    restaurant = models.ForeignKey(Restaurant)
    driver = models.ForeignKey(Driver, blank=True, null=True)  # can be blank
    address = models.CharField(max_length=500)
    total = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    picked_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, related_name='order_details')
    meal = models.ForeignKey(Meal)
    quantity = models.IntegerField()
    sub_total = models.IntegerField()

    def __str__(self):
        return str(self.id)