from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.payment import views


router = DefaultRouter()
router.register('cart', views.CartView, basename='cart')


urlpatterns = [
    path('', include(router.urls))
]
