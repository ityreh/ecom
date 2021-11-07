from core.utils import get_env_variable
from django.contrib import admin
from django.urls import include, path

ADMIN_PATH = get_env_variable('URLS_ADMIN_PATH')

urlpatterns = [
    path('products/', include('products.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    #TODO: docs
    #path('admin/doc', include('django.contrib.admin.docs.urls')),
    path(ADMIN_PATH, admin.site.urls),
]
