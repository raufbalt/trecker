from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from service.models import Service, Category
from service.serializers import ServiceSerializer, CategorySerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        data = self.request.data
        income = self.request.data.get("income", None)
        expense = self.request.data.get("expense", None)
        balance = int(income) - int(expense)

        category = self.request.data.get('category', None)
        category = int(category)
        category1 = get_object_or_404(Category, id=category)
        # serializer.save(
        #     expense=self.request.data.get("expense", None),
        #     expence_notice=self.request.data.get("expense_notice", None),
        #     income=self.request.data.get("income", None),
        #     balance=balance,
        #     date_created=self.request.data.get("date_created", None),
        #     date_modified=self.request.data.get("date_modified", None),
        #     category=category1,
        #
        # )
        Service.objects.create(
            expense=self.request.data.get("expense", None),
            expence_notice=self.request.data.get("expense_notice", None),
            income=self.request.data.get("income", None),
            balance=balance,
            date_created=self.request.data.get("date_created", None),
            date_modified=self.request.data.get("date_modified", None),
            category=category1,
        )


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]