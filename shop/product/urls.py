from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AddressViewSet, CategoryViewSet, CustomerViewSet, OrderViewSet, ProductViewSet, ShopViewSet, \
    login, UserViewSet

app_name = "articles"

router = DefaultRouter()
router.register('products', ProductViewSet, )
router.register('categories', CategoryViewSet)
router.register('shops', ShopViewSet)
router.register('orders', OrderViewSet)
router.register('addresses', AddressViewSet)
router.register('customers', CustomerViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls + [path('login/', login)]
