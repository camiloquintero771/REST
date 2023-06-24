from django.urls import path
from products.views.general_views import MeasureUnitListAPIView, CategoryProductListAPIView, IndicatorListAPIView
from products.views.product_views import ProductListAPIView
urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    path('product/', ProductListAPIView.as_view(), name='product'),
]