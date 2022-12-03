from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

User = get_user_model()

class Service(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #Расход
    expense = models.IntegerField(default=0)
    category = models.ForeignKey("category", on_delete=models.SET_NULL, null=True)
    expense_notice = models.CharField(max_length=50, null=True, blank=True)
    #Доход
    income = models.IntegerField(default=0)
    #Баланс
    # balance = models.IntegerField(default=income-expense)

    #Время создания и обновления
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name







