from django.urls import path, include
from .views import CustomerViewSet, CustomerDetailView

urlpatterns = [
    path('customers/', CustomerViewSet.as_view()),
    path('customers/<pk>', CustomerDetailView.as_view())
]

