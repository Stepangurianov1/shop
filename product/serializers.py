from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField
from .models import Product
from rest_framework import serializers


# class ProductModelSerializer(ModelSerializer):
#     url_field_name = serializers.EmailField()
#     class Meta:
#         model = Product
#         fields = '__all__'

class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class ProductModelSerializer(serializers.Serializer):
    objects = Product.objects.all()
    name = serializers.CharField(max_length=64)
    article = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    image = JSONSerializerField()
    status = serializers.CharField()
