from django.contrib import admin
from django.urls import NoReverseMatch, reverse
from django.utils.html import format_html

from .models import Product


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'label', 'size', 'price', 'quantity', 'status')

    #TODO: show url
    # readonly_fields = ('show_url',)

    # def show_url(self, instance):
    #     url = reverse('products:detail', kwargs={'pk': instance.pk})
    #     response = format_html("""<a href="{0}>{0}</a>""", url)
    #     return response

    # show_url.short_description = 'Product URL'
