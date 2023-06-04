from rest_framework.routers import DefaultRouter

from .views import TransportersAPIViewSet

router = DefaultRouter()
router.register(r'', TransportersAPIViewSet,
                basename='transpoters')

urlpatterns = router.urls
