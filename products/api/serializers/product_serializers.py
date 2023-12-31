from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state','created_date', 'modified_date', 'deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name':instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else' ',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.desciption,
        }