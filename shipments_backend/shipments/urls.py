from rest_framework.routers import DefaultRouter

from .views import ShipmentsAPIViewSet

router = DefaultRouter()
router.register(r'', ShipmentsAPIViewSet,
                basename='shipments')

urlpatterns = router.urls
