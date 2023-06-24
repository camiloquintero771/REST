from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'nombre_de_usuario': instance['username']
        }
