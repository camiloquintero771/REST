from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from users.api.serializers import UserAllSerializer

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserAllSerializer(user)
                if created:
                    return Response(
                        {'token': token.key,
                         'user': user_serializer.data,
                         'message':'Inicio de sesion exitoso'
                         }
                    )
                else:
                    token.delete()
                    token.objects.create(user=user)
            else:
                return Response({'error':'Este usuario no puede iniciar sesion'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseñas incorrectos'},
                            status=status.HTTP_401_UNAUTHORIZED)
        return Response({'mensaje':'Hola desde response'}, status=status.HTTP_200_OK)