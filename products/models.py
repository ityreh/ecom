from django.db import models
from django.db.models.deletion import CASCADE


class Product(models.Model):
    label = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')
    price = models.FloatField()
    quantity = models.IntegerField(default=0)


class Fabric(models.Model):
    label = models.CharField(max_length=200)
    product = models.ManyToManyField(Product)


class Pattern(models.Model):
    label = models.CharField(max_length=200)
    product = models.OneToOneField(Product, on_delete=CASCADE)


class ProductImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=CASCADE)


class FabricImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField()
    fabric = models.ForeignKey(Fabric, on_delete=CASCADE)


class PatternImage(models.Model):
    label = models.CharField(max_length=200)
    image = models.ImageField()
    pattern = models.ForeignKey(Pattern, on_delete=CASCADE)
