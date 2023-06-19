from django.urls import path
from core.utils.views import ResponseCodeView

urlpatterns = [
    path('response-codes/', ResponseCodeView.as_view(), name='response_codes')
]
