from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('products/', include('products.urls')),
    #TODO: docs
    #path('admin/doc', include('django.contrib.admin.docs.urls')),
    path('admin/', admin.site.urls),
]
