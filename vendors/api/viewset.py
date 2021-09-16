from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from vendors.api import serializers
from vendors import models


class VendorsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.VendorsSerializer
    queryset = models.Vendors.objects.all().order_by('id')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'cnpj', 'city']
