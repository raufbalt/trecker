
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from service.models import Service, Category, Expense, Income
from service.permissions import IsOwner
from service.serializers import ServiceSerializer, CategorySerializer, ExpenseSerializer, IncomeSerializer


class ServiceViewSet(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def perform_create(self, serializer):
        data = self.request.data

        Service.objects.create(
            owner = self.request.user,
            date_created=self.request.data.get("date_created", None),
  )

    def get_permissions(self):
        return [IsOwner()]


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'delete'):
            return [IsOwner()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        data = self.request.data

        service = self.request.data.get('service', None)
        service = int(service)
        service1 = get_object_or_404(Service, id=service)

        category = self.request.data.get('category', None)
        category1 = get_object_or_404(Category, slug=category)

        Expense.objects.create(

            owner=self.request.user,
            service = service1,
            created_date=self.request.data.get("created_date", None),
            value = self.request.data.get("value", None),
            category = category1,
	    expense_notice = self.request.data.get("expense_notice", None),
        )



class IncomeViewSet(ModelViewSet):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()

    def get_permissions(self):
        return [IsOwner()]

    def perform_create(self, serializer):
        data = self.request.data

        service = self.request.data.get('service', None)
        service = int(service)
        service1 = get_object_or_404(Service, id=service)

        Income.objects.create(

            owner=self.request.user,
            service=service1,
            created_date=self.request.data.get("created_date", None),
            value=self.request.data.get("value", None),
        )

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        return [permissions.IsAuthenticated()]
