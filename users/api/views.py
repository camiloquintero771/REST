from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .serializers import UserSerializer, UserDetailSerializer, UserAllSerializer
from users.models import User
from ..utils import decrypt_message


class UserAPIView(APIView):

    def get(self,request):
        users = User.objects.all()
        users_serialized = UserSerializer(users, many=True)
        return Response(users_serialized.data)

@api_view(['GET','POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.values("id","username")
        users_serialized = UserSerializer(users, many=True)
        return Response(users_serialized.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(request,pk):
    user = User.objects.filter(pk=pk).first()
    if user:
        if request.method == 'GET':
            #obtener 1 instancia
            user_serialized = UserDetailSerializer(user)
            return Response(user_serialized.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            # actualizar la instancia
            user_serialized = UserDetailSerializer(user, data=request.data)
            if user_serialized.is_valid():
                user_serialized.save()
                return Response(user_serialized.data, status=status.HTTP_200_OK)
            else:
                return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            #eliminar la instancia
            user.delete()
            return Response({'message':'Usuario eliminiado correctamente'},status=status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado usuario'}, status=status.HTTP_400_BAD_REQUEST)


class UserAllView(viewsets.ModelViewSet):
    serializer_class = UserAllSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            obj_user, key_value = serializer.save()
            messages = f'Producto creado exitosamente, la key para desencriptar es = {key_value} '
            return Response({'message': messages}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        padding_character = "{"
        user_obj = self.queryset.filter(pk=pk).first()

        key_value = user_obj.key
        key_encode = key_value.encode('utf-8')
        text_encryp = user_obj.text
        text_encryp_encode = text_encryp.encode('utf-8')
        text_decryp = decrypt_message(text_encryp_encode, key_encode, padding_character)
        user_obj.text_decrypt = text_decryp
        user_obj.save()
        user_serialized = self.serializer_class(user_obj)
        return Response(user_serialized.data, status=status.HTTP_200_OK)