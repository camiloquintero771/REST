from rest_framework.routers import DefaultRouter

from users.api.views import UserAllView
router = DefaultRouter()


router.register(r'user', UserAllView, basename='user')

urlpatterns = router.urls