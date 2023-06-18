from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.payment import views


router = DefaultRouter()
router.register('cart', views.CartView, basename='cart')
router.register('orders', views.OrderViewset, basename='orders')


urlpatterns = [
    path('', include(router.urls))
]
