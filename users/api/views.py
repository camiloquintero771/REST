from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from users.models import User

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
            user_serialized = UserSerializer(user)
            return Response(user_serialized.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            # actualizar la instancia
            user_serialized = UserSerializer(user, data=request.data)
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