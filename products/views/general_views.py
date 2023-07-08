from rest_framework import viewsets
from products.api.serializers.general_serializers import *


class MeasureUnitListAPIView(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer


class CategoryProductListAPIView(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer


class IndicatorListAPIView(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer