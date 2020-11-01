from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('suppliers/', views.SupplierListView.as_view(), name='suppliers'),
    path('supplier/<int:pk>', views.SupplierDetailView.as_view(), name='supplier-detail'),
]
