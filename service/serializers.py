from rest_framework import serializers

from service.models import Service, Category, Expense, Income


class ServiceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='auth.user')

    class Meta:
        model = Service
        fields = '__all__'

    def to_representation(self, instance):
        #Логика расхода
        try:
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
        except AttributeError:
            integ = [0]


        #------------------------------------------------------------------------


        #Логика Дохода
        try:
            summa_income = []
            integ_income = []
            for x in instance.polucheno.all().order_by('value').values():
                for y in x.items():
                    if "value" in y:
                        summa_income.append(y)
            for x in summa_income:
                for y in x:
                    if isinstance(y, int):
                        integ_income.append(y)
        except AttributeError:
            summa_income = [0]
            integ_income = [0]
        #--------------------------------------------------------------------------


        #Основная логика
        try:
            rep = super().to_representation(instance)
            print(summa_income, '!!!!!!!!')
            rep['income'] = sum(integ_income)
            rep['expense'] = sum(integ)
            rep['balance'] = sum(integ_income) - sum(integ)
            return rep
        except AttributeError:
            return rep
        #-------------------------------------------------------------------------


class IncomeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='auth.user')
    class Meta:
        model = Income
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='auth.user')
    class Meta:
        model = Expense
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'
