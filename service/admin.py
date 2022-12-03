from django.contrib import admin
from service.models import Service, Category, Expense

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Expense)