from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from products.api import serializers
from products import models


class ProductsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'code', 'price', 'vendor']
