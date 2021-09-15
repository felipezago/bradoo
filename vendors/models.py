from django.db import models
from localflavor.br.models import BRCNPJField


class Vendors(models.Model):
    name = models.CharField(max_length=255)
    cnpj = BRCNPJField(unique=True)
    city = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


