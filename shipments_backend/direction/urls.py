from rest_framework.routers import DefaultRouter

from .views import DirectionAPIViewSet

router = DefaultRouter()
router.register(r'', DirectionAPIViewSet, basename='directions')

urlpatterns = router.urls
