from django.contrib import admin
from django.urls import path
from myapp1.views import index_page, catalog_page, about_page, sotrud_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('catalog/', catalog_page),
    path('about/', about_page),
    path('sotrud/', sotrud_page)
]