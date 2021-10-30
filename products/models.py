import datetime
import uuid

from django.db import models
from django.db.models.deletion import CASCADE


class Product(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=200)
    publish_date = models.DateTimeField(
        default=datetime.datetime.now(), editable=False)
    size = models.CharField(max_length=10)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.label


class Fabric(models.Model):
    label = models.CharField(max_length=200)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.label


class Pattern(models.Model):
    label = models.CharField(max_length=200)
    product = models.OneToOneField(Product, on_delete=CASCADE)

    def __str__(self):
        return self.label


class ProductImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=CASCADE)

    def __str__(self):
        return self.label


class FabricImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField()
    fabric = models.ForeignKey(Fabric, on_delete=CASCADE)

    def __str__(self):
        return self.label


class PatternImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField()
    pattern = models.ForeignKey(Pattern, on_delete=CASCADE)

    def __str__(self):
        return self.label
