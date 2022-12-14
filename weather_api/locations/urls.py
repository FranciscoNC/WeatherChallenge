from rest_framework.routers import DefaultRouter
from locations.views import CountryViewSet, StateViewSet, CityViewSet

router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'states', StateViewSet, basename='state')
router.register(r'cities', CityViewSet, basename='city')
urlpatterns = router.urls
