from django.db import models
from django.urls import reverse


# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, blank=True)
    manager = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='inventories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("inventory:detail", kwargs={"pk": self.pk})


class Product(models.Model):
    price = models.IntegerField()
    inventory = models.ForeignKey('Inventory', on_delete=models.CASCADE, related_name='products')
    tag = models.ManyToManyField('Tag', related_name='products')

    def __str__(self):
        return f'{self.price} Rial - {self.inventory.name}'

    def get_absolute_url(self):
        return reverse("inventory:detail", kwargs={"pk": self.inventory.pk})


class Order(models.Model):
    weight = models.IntegerField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.weight} Kg - {self.product.price} Rial - {self.user.username}'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
