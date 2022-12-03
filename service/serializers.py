from rest_framework import serializers

from service.models import Service, Category


class ServiceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='auth.user')

    class Meta:
        model = Service
        fields = '__all__'

    def to_representation(self, instance):
        try:
            rep = super().to_representation(instance)
            rep['balance'] = instance.income - instance.expense
            return rep
        except AttributeError:
            return rep


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'