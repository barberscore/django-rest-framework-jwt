
# Third-Party
from rest_framework import routers

# Local
from .views import UserViewSet

router = routers.DefaultRouter(
    trailing_slash=False,
)

router.register(r'user', UserViewSet)
urlpatterns = router.urls