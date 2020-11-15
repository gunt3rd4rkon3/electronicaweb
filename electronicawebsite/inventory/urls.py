from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers'),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view(), name='supplier-detail'),
]

urlpatterns += [
    path('myproducts/', views.BoughtProductsByUserListView.as_view(), name='my-boughts'),
    path(r'available/', views.LoanedProductsAllListView.as_view(), name='all-available'),
]

urlpatterns += [
    path('product/<uuid:pk>/order/', views.order_product_worker, name='order-product-worker'),
]

urlpatterns += [
    path('supplier/create', views.SupplierCreate.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/update', views.SupplierUpdate.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/delete', views.SupplierDelete.as_view(), name='supplier_delete'),
]

urlpatterns += [
    path('product/create', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/update', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete', views.ProductDelete.as_view(), name='product_delete'),
]