from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import SalesData, Jokes

@admin.register(SalesData)
class SalesDataAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_item_id', 'quantity_ordered', 'item_price', 'promotion_discount', 'region', 'net_sale')
    search_fields = ('order_id', 'order_item_id', 'region')
    list_filter = ('region',)
    ordering = ('-net_sale',)

    def net_sale(self, obj):
        return obj.net_sale
    net_sale.admin_order_field = 'net_sale'
    net_sale.short_description = 'Net Sale'

@admin.register(Jokes)
class JokeAdmin(admin.ModelAdmin):
    list_display = ('category', 'joke_type', 'joke', 'setup', 'delivery', 'nsfw', 'political', 'sexist', 'safe', 'lang')
    search_fields = ('category', 'joke', 'setup', 'delivery')
