from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    #Расход
    expense = models.IntegerField(default=0)
    category = models.ForeignKey("category", on_delete=models.SET_NULL, null=True)
    expense_notice = models.CharField(max_length=50, null=True, blank=True)
    #Доход
    income = models.IntegerField(default=0)
    #Баланс
    # balance = models.IntegerField(default=income-expense)

    #Время создания и обновления
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(auto_now=True)


class Category(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=30, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name





