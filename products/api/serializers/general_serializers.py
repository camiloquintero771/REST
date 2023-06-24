from rest_framework import serializers

from products.models import MeasureUnit, CategoryProduct, Indicator


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('state',)


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        fields = ('state',)


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = ('state',)
