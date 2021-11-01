from django.contrib import admin

from .models import (Fabric, FabricImage, Pattern, PatternImage, Product,
                     ProductImage)


class FabricImageInline(admin.StackedInline):
    model = FabricImage
    extra = 1


class PatternImageInline(admin.StackedInline):
    model = PatternImage
    extra = 1


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    extra = 1


@admin.register(Pattern)
class PatternInline(admin.ModelAdmin):
    inlines = [PatternImageInline]


@admin.register(Fabric)
class FabricAdmin(admin.ModelAdmin):
    inlines = [FabricImageInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
