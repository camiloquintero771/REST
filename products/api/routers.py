from rest_framework.routers import DefaultRouter
from products.views.product_views import ProductViewset
from products.views.general_views import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView

router = DefaultRouter()

router.register(r'products', ProductViewset, basename='product')
router.register(r'measure_unit', MeasureUnitListAPIView, basename='product')
router.register(r'indicators', IndicatorListAPIView, basename='product')
router.register(r'category_products', CategoryProductListAPIView, basename='product')

urlpatterns = router.urls
