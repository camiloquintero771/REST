from django.urls import path
from .views import UserAPIView, user_api_view, user_detail_api_view

urlpatterns = [
    path('usuario/', UserAPIView.as_view(), name='user_api'),
    path('usuario_created/', user_api_view, name='user_api_fun'),
    path('usuario/<int:pk>', user_detail_api_view, name='user_detail')
]