from rest_framework import routers
from .api import LaunchViewSet

router = routers.DefaultRouter()
router.register('api/launch', LaunchViewSet, 'launch')

urlpatterns = router.urls