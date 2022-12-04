from django.contrib import admin
from service.models import Service, Category, Expense, Income

admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Expense)
admin.site.register(Income)