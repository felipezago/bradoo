from django.contrib import admin
from products.models import Products
from vendors.models import Vendors


class ProductInline(admin.TabularInline):
    model = Products
    raw_id_fields = ["vendor"]
    extra = 0


@admin.register(Vendors)
class VendorAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id", "name", "cnpj", "city"]
    list_filter = ["id", "name", "cnpj", "city"]
    search_fields = ["id", "name", "cnpj", "city"]
    inlines = [ProductInline]