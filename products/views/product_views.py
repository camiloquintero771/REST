from base.api import GenericListAPIView
from products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GenericListAPIView):
    serializer_class = ProductSerializer
