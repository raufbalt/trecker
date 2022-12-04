from rest_framework import serializers

from service.models import Service, Category, Expense


class ServiceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='auth.user')

    class Meta:
        model = Service
        fields = '__all__'

    def to_representation(self, instance):
        summa = []
        integ = []
        for x in instance.potracheno.all().order_by('value').values():
            for y in x.items():
                if "value" in y:
                    summa.append(y)
        for x in summa:
            for y in x:
                if isinstance(y, int):
                    integ.append(y)
        try:
            rep = super().to_representation(instance)
            print(summa, '!!!!!!!!', integ)
            rep['expense'] = sum(integ)
            rep['balance'] = instance.income - sum(integ)
            return rep
        except AttributeError:
            return rep

class ExpenseSerializer(ServiceSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'