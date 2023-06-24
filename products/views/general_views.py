from products.api.serializers.general_serializers import *
from base.api import GenericListAPIView


class MeasureUnitListAPIView(GenericListAPIView):
    serializer_class = MeasureUnitSerializer


class CategoryProductListAPIView(GenericListAPIView):
    serializer_class = CategoryProductSerializer


class IndicatorListAPIView(GenericListAPIView):
    serializer_class = IndicatorSerializer