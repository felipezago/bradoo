from rest_framework import serializers

from products.api.serializers import ProductsSerializer
from vendors import models


class VendorsSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = models.Vendors
        fields = (
            'id', 'name', 'cnpj', 'city', 'products'
        )



