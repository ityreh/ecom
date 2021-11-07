from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('products/', include('products.urls')),
    path('grappelli/', include('grappelli.urls')),
    #TODO: docs
    #path('admin/doc', include('django.contrib.admin.docs.urls')),
    path('admin/', admin.site.urls),
]
