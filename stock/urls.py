from django.urls import path, include

from .views import list_account, detail_account, create_account, edit_account, create_product, list_product, \
    detail_product, edit_product, delete_account, delete_product, left_add, left_sub

app_name = 'stock'

urlpatterns = [
    path('', list_product, name='list_product'),
    path('account/', list_account, name='list_account'),
    path('account/create/', create_account, name='create_account'),
    path('account/<int:pk>/', detail_account, name='detail_account'),
    path('account/<int:pk>/edit/', edit_account, name='edit_account'),
    path('account/<int:pk>/delete/', delete_account, name='delete_account'),
    path('product/create/', create_product, name='create_product'),
    path('product/<int:pk>/edit/', edit_product, name='edit_product'),
    path('product/<int:pk>/', detail_product, name='detail_product'),
    path('product/<int:pk>/delete/', delete_product, name='delete_product'),
    path('product/<int:pk>/add/', left_add, name='left_add'),
    path('product/<int:pk>/sub/', left_sub, name='left_sub'),
]
