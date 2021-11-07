from django.shortcuts import get_object_or_404, render

from .models import Product


def index(request):
    product_list = Product.objects.order_by('-created')[:12]
    context = {'product_list': product_list}
    return render(request, 'products/index.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})
