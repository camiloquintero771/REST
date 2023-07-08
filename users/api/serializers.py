from rest_framework import serializers
from users.models import User
from users.utils import generate_secret_key_for_AES_cipher, encrypt_message, decrypt_message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'nombre_de_usuario': instance['username']
        }


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk','username','email', 'name', 'last_name', 'phone', 'text', 'document')

    def to_representation(self, instance):
        return {
            'nombre_de_usuario': instance.username,
            'nombre': instance.name,
            'apellido': instance.last_name,
            'texto': instance.text_decrypt,
            'telefono': instance.phone,
            'cédula': instance.document
        }
    def create(self, validated_data):
        padding_character = "{"
        text = validated_data['text']
        key = generate_secret_key_for_AES_cipher()
        encrypted_msg = encrypt_message(text, key, padding_character)
        decrypted_msg = decrypt_message(encrypted_msg, key, padding_character)
        key_value = key.decode('utf-8')
        encrypted_msg_decode = encrypted_msg.decode('utf-8')
        print(encrypted_msg_decode)
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            name =validated_data['name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            text=encrypted_msg_decode,
            key=key_value,
            document=validated_data['email']
        )
        return user, key


