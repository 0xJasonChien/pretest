from django.urls import path

from api.views import import_order, import_product, list_product

urlpatterns = [
    path('import-order/', import_order),
    path('import-product/', import_product),
    path('list-product/', list_product),
]
