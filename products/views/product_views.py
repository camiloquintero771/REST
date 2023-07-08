from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import viewsets
from base.api import GenericListAPIView
from products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GenericListAPIView):
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message':'Producto creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        obj_product = self.get_queryset().filter(pk=pk).first()
        user_serialized = self.serializer_class(obj_product)
        return Response(user_serialized.data, status=status.HTTP_200_OK)

class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        product_object = self.get_queryset().filter(pk=pk).first()
        if product_object:
            product_object.state=False
            product_object.save()
            return Response({'message:producto eliminado'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe el producto'}, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer


    def get_queryset(self,):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def patch(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        obj_product = self.get_queryset().filter(pk=pk).first()
        if obj_product:
            user_serialized = self.serializer_class(obj_product)
            return Response(user_serialized.data, status=status.HTTP_200_OK)
        return Response({'error': 'No existe el producto'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        obj_product = self.get_queryset().filter(pk=pk).first()
        user_serialized = self.serializer_class(obj_product, data=request.data)
        if user_serialized.is_valid():
            user_serialized.save()
            return Response(user_serialized.data, status=status.HTTP_200_OK)
        return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        list_obj = self.serializer_class.Meta.model.objects.filter(state=True)
        return list_obj

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Producto creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        obj_product = self.get_queryset().filter(pk=pk).first()
        user_serialized = self.serializer_class(obj_product, data=request.data)
        if user_serialized.is_valid():
            user_serialized.save()
            return Response(user_serialized.data, status=status.HTTP_200_OK)
        return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        product_object = self.get_queryset().filter(pk=pk).first()
        if product_object:
            product_object.state = False
            product_object.save()
            return Response({'message:producto eliminado'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe el producto'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        product_serializer_list = self.get_serializer(self.get_queryset(), many=True)
        return Response(product_serializer_list.data, status=status.HTTP_200_OK)