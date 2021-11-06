from django.db import models
from model_utils import Choices
from model_utils.models import StatusField, TimeStampedModel, UUIDField


class TimeStampedImageModel(TimeStampedModel):
    pass


class Image(TimeStampedModel):
    label = models.CharField(max_length=200)
    model = models.ForeignKey(TimeStampedImageModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    width = models.FloatField(default=300)
    length = models.FloatField(default=300)

    def __str__(self):
        return self.label


class Product(TimeStampedImageModel):
    STATUS = Choices('anounced', 'available', 'sold', 'orderable')

    uuid = UUIDField(primary_key=True, version=4, editable=False)
    label = models.CharField(max_length=200)
    size = models.CharField(max_length=10)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    status = StatusField()

    def __str__(self):
        return self.label


class Fabric(TimeStampedImageModel):
    label = models.CharField(max_length=200)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


class Pattern(TimeStampedImageModel):
    label = models.CharField(max_length=200)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
