from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from service.models import Service, Category, User, Expense
from service.permissions import IsOwner
from service.serializers import ServiceSerializer, CategorySerializer, ExpenseSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        data = self.request.data

        category = self.request.data.get('category', None)
        category1 = get_object_or_404(Category, slug=category)
        Service.objects.create(
            owner = self.request.user,
            expense=self.request.data.get("expense", None),
            expense_notice=self.request.data.get("expense_notice", None),
            income=self.request.data.get("income", None),
            date_created=self.request.data.get("date_created", None),
            date_modified=self.request.data.get("date_modified", None),
            category=category1,

        )

    def get_permissions(self):
        return [IsOwner()]


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()






class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]