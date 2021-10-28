from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def index(request):
    product_list = Product.objects.order_by('-publish_date')[:12]
    output = ', '.join([product.label for product in product_list])
    return HttpResponse(output)


def detail(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)
