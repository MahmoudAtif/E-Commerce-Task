from django.urls import path
from core.users import views


urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign-up')
]
