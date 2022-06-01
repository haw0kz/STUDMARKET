from django.urls import path
from products.views import products,basket_add,basket_delete,prodvoz,prodyb

app_name = 'products'

urlpatterns = [
    path('<int:category_id>/', products, name='category'),
    path('', products, name = 'index'),
    path('prodvoz/', prodvoz, name = 'prodvoz'),
    path('prodyb/', prodyb, name = 'prodyb'),
    path('basket-add/<int:product_id>/', basket_add, name = 'basket_add'),
    path('basket-delete/<int:id>/', basket_delete, name = 'basket_delete'),

]

