import uuid

from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields.related import ForeignKey
from django.utils.timezone import now


class ProductImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.label


class FabricImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.label


class PatternImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.label


class Fabric(models.Model):
    label = models.CharField(max_length=200)
    images = ForeignKey(FabricImage, on_delete=CASCADE)

    def __str__(self):
        return self.label


class Pattern(models.Model):
    label = models.CharField(max_length=200)
    images = ForeignKey(PatternImage, on_delete=CASCADE)

    def __str__(self):
        return self.label


class Product(models.Model):
    product_id = models.UUIDField(default=uuid.uuid4, editable=False)
    label = models.CharField(max_length=200)
    publish_date = models.DateTimeField(
        default=now, editable=False)
    size = models.CharField(max_length=10)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    pattern = models.ForeignKey(Pattern, on_delete=PROTECT)
    fabrics = models.ManyToManyField(Fabric)
    images = ForeignKey(ProductImage, on_delete=CASCADE)

    def __str__(self):
        return self.label
