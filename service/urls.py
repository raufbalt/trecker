from django.urls import path, include

from .views import ServiceViewSet, CategoryViewSet, IncomeViewSet, ExpenseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('service', ServiceViewSet)
router.register('categories', CategoryViewSet)
router.register('income', IncomeViewSet)
router.register('expense', ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls))
]
